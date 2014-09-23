import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from college_life.forms import BasicAttackForm, SkillUseForm, FleeForm, EmailUserCreationForm, CharacterCreationForm
from college_life.models import Zone, Mob, Character, Monster, Major


def level_up(character):
    character.level += 1
    character.save()
    stats = character.major.stat_change(character.level)
    hp_mp_change = character.stat_change()
    character.str = stats['str']
    character.int = stats['int']
    character.agl = stats['agl']
    character.xp_next = character.level_xp_needed()
    character.hp_max = hp_mp_change['hp']
    character.mp_max = hp_mp_change['mp']
    character.hp = character.hp_max
    character.mp = character.mp_max
    character.save()


def monster_update(base_mob, user_mob):
    multiplier = 1.1
    hp = base_mob.hp
    level = base_mob.zone.level
    user_mob.name = base_mob.name
    user_mob.hp = level * (hp + (level-1)) + (hp * (level-1))
    user_mob.level = level
    user_mob.xp_drop = base_mob.zone.get_xp()
    user_mob.gp_drop = base_mob.zone.get_gp()
    user_mob.basic_attack = base_mob.basic_attack
    user_mob.int = int(base_mob.int + ((level - 1) * base_mob.int * multiplier))
    user_mob.str = int(base_mob.str + ((level - 1) * base_mob.str * multiplier))
    user_mob.agl = int(base_mob.agl + ((level - 1) * base_mob.agl * multiplier))
    user_mob.attack_description = base_mob.attack_description
    user_mob.image = base_mob.image
    user_mob.save()


def check_results(character, monster):
    if monster.hp <= 0:
        character.xp += monster.xp_drop
        character.gp += monster.gp_drop
        character.save()
        return "win"
    if character.hp <= 0:
        character.hp = character.hp_max
        character.save()
        return "lose"


def fight(character, monster, attack_type, multiplier):
    stats = {
        'int': (character.int, monster.int),
        'str': (character.str, monster.str),
        'agl': (character.agl, monster.agl),
    }
    attack = stats[attack_type][0] + (multiplier * character.level)
    defence = stats[attack_type][1]
    damage = int(attack - defence + 1)
    if damage < 0:
        damage = 0

    monster.hp -= damage
    if monster.hp < 0:
        monster.hp = 0
    monster.save()

    return damage


def what_action(does_hit, does_skill, does_run):
    if does_hit is not None and does_hit != "":
        return 'hit'
    if does_skill is not None:
        return 'skill'
    if does_run is not None and does_run != "":
        return 'run'


def register(request):
    data = {
        'user_form': EmailUserCreationForm(prefix='user'),
        'character_form': CharacterCreationForm(prefix='character')
    }
    if request.method == 'POST':
        user_form = EmailUserCreationForm(request.POST, prefix='user')
        character_form = CharacterCreationForm(request.POST, prefix='character')
        if user_form.is_valid() and character_form.is_valid():
            user = user_form.save()
            character = Character(user=user, name=character_form.cleaned_data['name'], major=character_form.cleaned_data['major'])
            level_up(character)
            monster = Monster(user=user, name='starter')
            monster.save()
            # text_content = 'Thank you for signing up for our website, {} {}'.format(user.first_name, user.last_name)
            # html_content = '<h2>Thanks {} {} for signing up!</h2> <div>I hope you enjoy using our site</div>'.format(user.first_name, user.last_name)
            # msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            return redirect("profile")
        else:
            data = {
                'user_form': user_form,
                'character_form': character_form
            }

    return render(request, "registration/register.html", data)


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def map(request):
    character = request.user.character
    zones = Zone.objects.filter(level__lte=character.level)
    # zones = Zone.objects.all()
    data = {
        'zones': zones,
    }
    return render(request, 'map.html', data)


@login_required
def zone(request, zone_id):
    mob = Mob.objects.filter(zone=zone_id).order_by('?')[0]
    monster = request.user.monster
    monster_update(mob, monster)
    return redirect("combat_test")


@login_required
def combat_run(request):
    character = request.user.character
    drop = int(character.gp * 0.10)
    character.gp -= drop
    character.save()
    data = {
        'drop': drop,
    }
    return render(request, 'run.html', data)


@login_required
def stats(request):
    return render(request, 'stats.htm')


@login_required
def dorm(request):
    character = request.user.character
    character.hp = character.hp_max
    character.save()
    return render(request, 'dorm.html')


@login_required
def bar(request):
    character = request.user.character
    character.mp = character.mp_max
    character.save()
    return render(request, 'bar.html')


def faq(request):
    data = {
        'physics': Major.objects.get(pk=1),
        'compsci': Major.objects.get(pk=2),
        'sports': Major.objects.get(pk=3),
        'dance': Major.objects.get(pk=4),
        'drama': Major.objects.get(pk=5),
        'art': Major.objects.get(pk=6),
    }
    return render(request, 'faq.html', data)


def splash(request):
    return render(request, 'splash.html')


def test(request):
    return render(request, 'test.html')


def combat_action(request):
    character = request.user.character
    monster = request.user.monster
    basic_hit = ''
    skill_hit = ''
    run = ''
    monster_hit = ''
    win_text = ''
    lose_text = ''
    monster_damage = 0
    player_damage = 0
    data = {'basic_hit': basic_hit,
            'skill_hit': skill_hit,
            'run': run,
            'win_text': win_text,
            'lose_text': lose_text,
            'monster_damage': monster_damage,
            'player_damage': player_damage,
            'monster_hit': monster_hit,
            'attack_form': BasicAttackForm(prefix='basic'),
            'skill_form': SkillUseForm(character=character, prefix='skill'),
            'run_form': FleeForm(prefix='flee'),
            }
    if request.method == "POST":
        basic_attack = BasicAttackForm(request.POST, prefix='basic')
        skill_attack = SkillUseForm(request.POST, character=character, prefix='skill')
        flee = FleeForm(request.POST, prefix='flee')

        if basic_attack.is_valid() and skill_attack.is_valid() and flee.is_valid():
            does_hit = basic_attack.cleaned_data['attack']
            does_skill = skill_attack.cleaned_data['skills']
            does_run = flee.cleaned_data['run']
            action = what_action(does_hit, does_skill, does_run)

            if action is 'hit':
                attack_type = character.major.basic_attack
                monster_damage = fight(character, monster, attack_type, 0)
                basic_hit = 'you strike with your weapon'

            if action is 'skill':
                if does_skill.cost <= character.mp:
                    attack_type = does_skill.kind
                    multiplier = does_skill.multiplier
                    monster_damage = fight(character, monster, attack_type, multiplier)
                    character.mp -= does_skill.cost
                    if character.mp < 0:
                        character.mp = 0
                    skill_hit = does_skill
                else:
                    skill_hit = "you don't have enough liquid courage under your belt to pull this off"

            if action is 'run':
                flee_odds = 0.5 + 0.1*(character.level - monster.level)
                can_flee = random.random()
                if can_flee < flee_odds:
                    return redirect("run")
                else:
                    run = "You are unable to run away..."

            if monster.hp > 0:
                attack_type = monster.basic_attack
                player_damage = fight(monster, character, attack_type, 0)
                monster_hit = 'attacks'

            result = check_results(character, monster)
            if result is 'win':
                win_text = 'win'
                if character.xp >= character.xp_next:
                    level_up(character)
            elif result is 'lose':
                loss = int(character.gp * 0.07)
                character.gp -= loss
                lose_text = loss
                character.save()

            data = {'basic_hit': basic_hit,
                    'skill_hit': skill_hit,
                    'run': run,
                    'win_text': win_text,
                    'lose_text': lose_text,
                    'monster_damage': monster_damage,
                    'player_damage': player_damage,
                    'monster_hit': monster_hit,
                    'attack_form': BasicAttackForm(prefix='basic'),
                    'skill_form': SkillUseForm(character=character, prefix='skill'),
                    'run_form': FleeForm(prefix='flee'),
                    }

            return render(request, "combat_test.html", data)
        else:
            data = {'basic_hit': '',
                    'skill_hit': '',
                    'run': run,
                    'win_text': win_text,
                    'lose_text': lose_text,
                    'monster_damage': monster_damage,
                    'player_damage': player_damage,
                    'monster_hit': monster_hit,
                    'attack_form': basic_attack,
                    'skill_form': skill_attack,
                    'run_form': flee,
                    }
    return render(request, "combat_test.html", data)