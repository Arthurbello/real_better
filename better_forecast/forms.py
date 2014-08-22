from django import forms
from django.contrib.auth.forms import UserCreationForm
from better_forecast.models import BetterUser
from django.forms.formsets import formset_factory

class WeatherUserCreationForm(UserCreationForm):
        email = forms.EmailField(required=True)
        # don't need to recreate all of these fields since it's a model form
        PART_CHOICES = (
        ('RANDOM', 'Random'),
        ('YOURCHOICE', 'Yourchoice'),)
        PART_STATE = (
        ('AL', 'AL'),
        ('AK', 'AK'),
        ('AZ', 'AZ'),
        ('AR', 'AR'),
        ('CA', 'CA'),
        ('CO', 'CO'),
        ('CT', 'CT'),
        ('DE', 'DE'),
        ('FL', 'FL'),
        ('GA', 'GA'),
        ('HI', 'HI'),
        ('ID', 'ID'),
        ('IL', 'IL'),
        ('IN', 'IN'),
        ('IA', 'IA'),
        ('KS', 'KS'),
        ('KY', 'KY'),
        ('LA', 'LA'),
        ('ME', 'ME'),
        ('MD', 'MD'),
        ('MA', 'MA'),
        ('MI', 'MI'),
        ('MN', 'MN'),
        ('MS', 'MS'),
        ('MO', 'MO'),
        ('MT', 'MT'),
        ('NE', 'NE'),
        ('NV', 'NV'),
        ('NH', 'NH'),
        ('NJ', 'NJ'),
        ('NM', 'NM'),
        ('NY', 'NY'),
        ('NC', 'NC'),
        ('ND', 'ND'),
        ('OH', 'OH'),
        ('OK', 'OK'),
        ('OR', 'OR'),
        ('PA', 'PA'),
        ('RI', 'RI'),
        ('SC', 'SC'),
        ('SD', 'SD'),
        ('TN', 'TN'),
        ('TX', 'TX'),
        ('UT', 'UT'),
        ('VT', 'VT'),
        ('VA', 'VA'),
        ('WA', 'WA'),
        ('WV', 'WV'),
        ('WI', 'WI'),
        ('WY', 'WY')
        )
        choice = forms.ChoiceField(choices=PART_CHOICES, required=True, label='What\'s your choice?')
        state = forms.ChoiceField(choices=PART_STATE, required=True, label='State')
        city = forms.CharField(max_length=25)
        class Meta:
            model = BetterUser
            fields = ("username", "email", "state", "city", "password1",
                      "password2", "choice")

        def clean_username(self):
            # Since User.username is unique, this check is redundant,
            # but it sets a nicer error message than the ORM. See #13147.
            username = self.cleaned_data["username"]
            try:
                BetterUser.objects.get(username=username)
            except BetterUser.DoesNotExist:
                return username
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',
            )


# Could make these model forms instead
class RainFavouriteForm(forms.Form):
    choice1 = forms.CharField(max_length=160)

RainFavouriteSet = formset_factory(RainFavouriteForm, extra=9)


class SunFavouriteForm(forms.Form):
    choice2 = forms.CharField(max_length=160)

SunFavouriteSet = formset_factory(SunFavouriteForm, extra=9)


class SnowFavouriteForm(forms.Form):
    choice3 = forms.CharField(max_length=160)

SnowFavouriteSet = formset_factory(SnowFavouriteForm, extra=9)
