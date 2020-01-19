from django.forms import ModelForm
from .models import SellHarvestedCrops
from django import forms


class SaleForm(ModelForm):
    """
    Django based forms Sale Form for rendering form from models on templates
    """
    Harvest_Variety = forms.CharField(
        label='Enter Specific Variety of Crop ',
        widget=forms.TextInput(attrs={'placeholder': 'For example Alphonso is  specific variety of Mango'})
    )

    class Meta:
        model = SellHarvestedCrops
        fields = (
        'Quantity', 'Harvest_Type', 'Crop_Name', 'Harvest_Variety', 'Harvest_Description', 'quality', 'sold_by',
        'Farm_image')
