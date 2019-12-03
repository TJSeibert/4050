from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class ProfileUpdateForm(forms.ModelForm):
    billing_address = forms.CharField()
    promo_register = forms.CheckboxInput()
    card_number = forms.CharField()

    class Meta:
        model = Profile
        fields = ['image', 'billing_address', 'card_number', 'promo_register']
