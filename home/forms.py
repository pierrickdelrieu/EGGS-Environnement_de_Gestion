from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import UserManager


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'botom_user'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)  # boite de caractères masqués


class SigninForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=30)
    last_name = forms.CharField(label="Nom", max_length=30)
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)  # boite de caractères masqués
    password2 = forms.CharField(label="Confirmation de mot de passe", widget=forms.PasswordInput)
