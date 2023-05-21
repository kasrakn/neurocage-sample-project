from django import forms
from webApp.models import Cage


class CreateCageForm(forms.ModelForm):
    label = forms.CharField(
        max_length=255,
        label='Cage Label',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Label of the cage'
            }
        )
    )

    class Meta:
        model = Cage
        fields = ('label',)


class UpdateCageForm(forms.ModelForm):
    label = forms.CharField(
        max_length=255,
        label='New Label',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Label of the cage'
            }
        )
    )

    class Meta:
        model = Cage
        fields = ('label',)