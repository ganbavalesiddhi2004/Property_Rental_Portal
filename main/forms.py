
from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = [
            'category',
            'title',
            'description',
            'area',
            'approximate_rent',
        ]

        widgets = {
            'category': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter property title'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Describe the property'
                }
            ),
            'area': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Example: Rajarampuri, Kolhapur'
                }
            ),
            'approximate_rent': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Monthly rent in ₹',
                    'min': '0',
                    'step': '0.01'
                }
            ),
        }


# area form
from django import forms
from .models import AvailableArea


class AvailableAreaForm(forms.ModelForm):
    class Meta:
        model = AvailableArea
        fields = ['name', 'description', 'display_order', 'is_active']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter area name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter area description'
            }),
            'display_order': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }