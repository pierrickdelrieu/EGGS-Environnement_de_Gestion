from django import forms
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


from .models import *
from django.contrib.auth import authenticate, login, password_validation

from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.CharField(label="Email", max_length=30,
                            widget=forms.TextInput(attrs={'class': 'botom_user'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)  # boite de caractères masqués

    def log(self, request) -> bool:
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        user = authenticate(username=email, password=password)  # vérifications si les données sont corrects
        if user:  # si user ≠ None
            login(request, user)
            return True
        return False


class SigninForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=30, widget=forms.TextInput(
        attrs={'placeholder': "Entrer votre prénom"}))
    last_name = forms.CharField(label="Nom", max_length=30, widget=forms.TextInput(
        attrs={'placeholder': "Entrer votre nom de famille"}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(
        attrs={'placeholder': "Entrer votre email"}))
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(
        attrs={'placeholder': "Entrer votre mot de passe"}))  # boite de caractères masqués
    password2 = forms.CharField(label="Confirmation de mot de passe", widget=forms.PasswordInput(
        attrs={'placeholder': "Confirmer votre mot de passe"}))

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                _('Les deux mot de passe sont différents'),
                code='password_mismatch',
            )
        return password2

    def clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data['password2']
        if password:
            try:
                password_validation.validate_password(password)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self):
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password1"]
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]

        new_user = Manager()
        new_user.create_user(first_name=first_name, last_name=last_name, email=email,
                             password=password)


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
