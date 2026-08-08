from django import forms
from .models import Appliance


class ApplianceForm(forms.ModelForm):

    class Meta:
        model = Appliance
        fields = [
            'name',
            'power_watts',
            'hours_per_day',
            'days_per_month',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Example: AC'
            }),

            'power_watts': forms.NumberInput(attrs={
                'placeholder': 'Example: 1500',
                'min': '0'
            }),

            'hours_per_day': forms.NumberInput(attrs={
                'placeholder': 'Example: 6',
                'min': '0',
                'max': '24',
                'step': '0.1'
            }),

            'days_per_month': forms.NumberInput(attrs={
                'placeholder': 'Example: 30',
                'min': '1',
                'max': '31'
            }),
        }