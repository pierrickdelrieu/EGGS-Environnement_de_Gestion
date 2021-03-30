from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class UserManager(models.Model):
    userModel = models.OneToOneField(User,
                                     on_delete=models.CASCADE)  # liaison avec le modele user prédéfini dans django
    ''' - username : nom d'utilisateur, 30 caractères maximum (lettre, chiffre et caractères spéciaux)
        - first_name : prénom, optionnel, 30 caractères maximum
        - last_name : nom de famille, optionnel, 30 caract!res maximum
        - email : adresse email
        - password : un hash du mot de passe'''

