import random
from django.contrib.auth.models import User
from django.db import models


class Major(models.Model):
    name = models.CharField(max_length=20)
    str = models.IntegerField(default=0)
    str_multiplier = models.FloatField(default=0)
    int = models.IntegerField(default=0)
    int_multiplier = models.FloatField(default=0)
    agl = models.IntegerField(default=0)
    agl_multiplier = models.FloatField(default=0)
    basic_attack = models.CharField(max_length=3)
    attack_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='major_images', blank=True, null=True)

    def stat_change(self, level):
        stats = {
            'str': self.str + (self.str * (level-1) * self.str_multiplier),
            'int': self.int + (self.int * (level-1) * self.int_multiplier),
            'agl': self.agl + (self.agl * (level-1) * self.agl_multiplier),
        }
        return stats

    def __unicode__(self):
        return u"{}".format(self.name)


class Skill(models.Model):
    major = models.ForeignKey(Major, null=True, blank=True, related_name='skills')
    name = models.CharField(max_length=120)
    level = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    kind = models.CharField(max_length=3)
    multiplier = models.FloatField(default=0)

    def __unicode__(self):
        return u"{}, ({})".format(self.name, self.cost)


class Character(models.Model):
    name = models.CharField(max_length=120)
    major = models.ForeignKey(Major, related_name='characters')
    user = models.OneToOneField(User, null=True, blank=True, related_name='character')
    xp = models.IntegerField(default=0)
    xp_next = models.IntegerField(default=0)
    hp = models.IntegerField(default=0)
    hp_max = models.IntegerField(default=0)
    mp = models.IntegerField(default=0)
    mp_max = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    gp = models.IntegerField(default=0)
    str = models.IntegerField(default=0)
    int = models.IntegerField(default=0)
    agl = models.IntegerField(default=0)

    def level_xp_needed(self):
        return self.level**2 * 10000

    def stat_change(self):
        change = {
            'hp': self.level * (10+(self.level-1)) + (10*(self.level-1)),
            'mp': self.level * (1+(self.level-1)) + 5,
        }
        return change

    def __unicode__(self):
        # return u"{}, {}, {}".format(self.user.username, self.name, self.major)
        return u"{}, {}".format(self.name, self.major)


class Monster(models.Model):
    name = models.CharField(max_length=120)
    user = models.OneToOneField(User, null=True, blank=True, related_name='monster')
    xp_drop = models.IntegerField(default=0)
    gp_drop = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    hp = models.IntegerField(default=0)
    str = models.IntegerField(default=0)
    int = models.IntegerField(default=0)
    agl = models.IntegerField(default=0)
    basic_attack = models.CharField(max_length=3, null=True, blank=True)
    attack_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='monster_images', blank=True, null=True)

    def __unicode__(self):
        return u"{}, {}, {}".format(self.user.username, self.user.character.name, self.name)


class Zone(models.Model):
    name = models.CharField(max_length=120)
    level = models.IntegerField(default=1)
    xp_drop = models.IntegerField(default=0)
    gp_drop = models.IntegerField(default=0)
    image = models.ImageField(upload_to='zone_images', blank=True, null=True)

    def get_xp(self):
        xp_base = 250 + ((self.level - 1)*500)
        random_range = 1.0 + ((random.random() - 0.5) * 0.2)
        print int(random_range * xp_base)
        return int(random_range * xp_base)

    def get_gp(self):
        gp_base = self.level**2 * 25
        random_range = 1.0 + ((random.random() - 0.5) * 0.5)
        print int(random_range * gp_base)
        return int(random_range * gp_base)

    def __unicode__(self):
        return u"{}".format(self.name)


class Mob(models.Model):
    name = models.CharField(max_length=120)
    zone = models.ForeignKey(Zone, related_name='mobs')
    hp = models.IntegerField(default=0)
    str = models.IntegerField(default=0)
    int = models.IntegerField(default=0)
    agl = models.IntegerField(default=0)
    basic_attack = models.CharField(max_length=3)
    attack_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='monster_images', blank=True, null=True)

    def __unicode__(self):
        return u"{}, {}".format(self.zone, self.name)
