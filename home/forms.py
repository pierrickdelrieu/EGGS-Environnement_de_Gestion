from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm

from .models import UserManager
from .passwordValidator import check_password_condition
from django.contrib.auth import authenticate, login


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'botom_user'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)  # boite de caractères masqués

    def log(self, request) -> bool:
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        user = authenticate(username=username, password=password)  # vérifications si les données sont corrects
        if user:  # si user ≠ None
            login(request, user)
            return True
        return False


class SigninForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=30)
    last_name = forms.CharField(label="Nom", max_length=30)
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)  # boite de caractères masqués
    password2 = forms.CharField(label="Confirmation de mot de passe", widget=forms.PasswordInput)

    def signup(self):
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"].lower()
        password1 = self.cleaned_data["password1"]
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]

        new_user = User.objects.create_user(username, email, password1)
        new_user.first_name = first_name
        new_user.last_name = last_name

        if new_user:  # si user ≠ None
            user = UserManager(userModel=new_user)
            user.save()

    def check_error(self) -> str:
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"].lower()
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        # Vérification si le nom d'utilisateur n'est pas déjà existant
        if User.objects.filter(username=username).exists():
            return "username"

        # Vérification si l'email n'est pas déjà existant
        elif User.objects.filter(email=email).exists():
            return "email"

        # Vérification de la confirmation du mot de passe
        elif password1 != password2:
            return "different_password"

        elif not check_password_condition(password1):
            return "password_condition"

        return "None"


# Redéfinition
# cf. : https://django-wiki.readthedocs.io/en/0.2.2/_modules/django/contrib/auth/forms.html
class PasswordResetConfirmationForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput,
    )
    new_password2 = forms.CharField(
        label="Confirmation de mot de passe",
        widget=forms.PasswordInput,
    )


# Redefinition
# cf. : https://django-wiki.readthedocs.io/en/0.2.2/_modules/django/contrib/auth/forms.html
class PasswordResetFormEmail(PasswordResetForm):
    email = forms.EmailField(label="Email", max_length=254)
