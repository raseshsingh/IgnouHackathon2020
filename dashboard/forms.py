from django import forms
from .models import Vegetable


class VegetableForm(forms.ModelForm):
    class Meta:
        model = Vegetable
        fields = ('name', 'quantity', 'description', 'image', 'price')
