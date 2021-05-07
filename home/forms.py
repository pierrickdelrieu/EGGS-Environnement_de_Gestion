from django import forms
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from .models import *
from django.contrib.auth import authenticate, login, password_validation

from django.contrib.auth import get_user_model
User = get_user_model()  # new User definitions


class LoginForm(forms.Form):
    email = forms.CharField(label="Email", max_length=30, widget=forms.TextInput)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)  # boite de caractères masqués

    # Error if the account is not active
    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if email and User.objects.filter(email=email).exists():
            user = Manager.objects.filter(email=email).get()
            if not user.is_active:
                raise ValidationError(
                    _("Vous n'avez pas validé votre compte par email"),
                    code='user_is_not_active',
                )
        return email

    def clean_password(self):
        email = self.cleaned_data.get("email").lower()
        password = self.cleaned_data.get("password")
        user = authenticate(username=email, password=password)  # vérifications si les données sont corrects
        if not user:  # si user ≠ None
            raise ValidationError(
                _("Adresse email ou mot de passe invalide"),
                code='invalid_auth',
            )
        return password


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

    # Error if the password confirmation is not valid
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                _('Les deux mot de passe sont différents'),
                code='password_mismatch',
            )
        return password2

    # Error if the email is already existing in the database
    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        if email and User.objects.filter(email=email).exists():
            raise ValidationError(
                _("L'email est deja existant"),
                code='email_exist',
            )
        return email

    def clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password)
            except ValidationError as error:
                self.add_error('password2', error)

    # User registration in memory. If commit = True, save in the database
    def save(self, commit: bool):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password1")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")

        new_user = Manager()
        new_user.set(first_name=first_name, last_name=last_name, email=email)
        new_user.set_password(password)

        if commit:
            new_user.save()

        return new_user


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

    # Error if the password confirmation is not valid
    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    _('Les deux mot de passe sont différents'),
                    code='password_mismatch',
                )
        password_validation.validate_password(password2, self.user)
        return password2


# Redefinition
# cf. : https://django-wiki.readthedocs.io/en/0.2.2/_modules/django/contrib/auth/forms.html
class PasswordResetFormEmail(PasswordResetForm):
    email = forms.EmailField(label="Email", max_length=254)
