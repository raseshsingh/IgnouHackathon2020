from django import forms
from django.contrib.auth.models import User
from .models import FarmerBuyerAccount


class ProfileForm(forms.ModelForm):
    class Meta:
        model = FarmerBuyerAccount
        fields = ('user_type', 'Farm_City', 'Address')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
