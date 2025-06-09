from django.forms import ModelForm
from django import forms
from orphanage_administrator.models import Person


TRUE_OR_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [
            "name",
            "rut",
            "mistreats_animals"
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-textinput'}),
            'rut': forms.TextInput(attrs={'class': 'form-textinput'}),
            'mistreats_animals': forms.Select(
                choices=((True, 'Sí'), (False, 'No'))
            )
        }
