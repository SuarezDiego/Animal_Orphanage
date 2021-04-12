from django.forms import ModelForm
from django import forms
from orphanage_administrator.models import Animal


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = [
            "name",
            "description",
            "picture_url",
            "date_found",
            "place_found"
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-textinput'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea'}),
            'picture_url': forms.URLInput(attrs={'class': 'form-textinput'}),
            'date_found': forms.NumberInput(attrs={'type': 'date'}),
            "place_found": forms.TextInput(attrs={'class': 'form-textinput'})
        }

class AdoptForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdoptForm, self).__init__(*args, **kwargs)
        self.fields['owner'].queryset = (
            self.fields['owner'].queryset.exclude(mistreats_animals=True)
        )
    class Meta:
        model = Animal
        fields = ['date_adoption','owner']
        widgets = {
            'date_adoption': forms.NumberInput(attrs={'type': 'date'}),
        }