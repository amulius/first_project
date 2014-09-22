from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from college_life.models import Skill, Major


class SimpleInput(forms.Form):
    question = forms.CharField(max_length=120)


class BasicAttackForm(forms.Form):
    attack = forms.CharField(widget=forms.HiddenInput(), required=False, initial='Hit')


class FleeForm(forms.Form):
    run = forms.CharField(widget=forms.HiddenInput(), required=False, initial='Run')


class SkillUseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        character = kwargs.pop('character', None)
        # mp = kwargs.pop('mp', None)
        super(SkillUseForm, self).__init__(*args, **kwargs)
        self.fields['skills'] = forms.ModelChoiceField(Skill.objects.
                                                       filter(major=character.major).
                                                       filter(level__lte=character.level).
                                                       filter(cost__lte=character.mp), required=False)


class CharacterCreationForm(forms.Form):
    name = forms.CharField(max_length=20, required=True, label="Character's name")
    major = forms.ModelChoiceField(Major.objects.all(), required=True, label="Character's major")


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )