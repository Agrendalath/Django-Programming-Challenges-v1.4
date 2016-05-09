from django import forms

from .models import FirstName, Country


class NameGenerationForm(forms.Form):
    sex = forms.ChoiceField(choices=FirstName.SEX, widget=forms.RadioSelect)
    country = forms.ChoiceField(choices=Country.objects.all().values_list('id', 'name'))
