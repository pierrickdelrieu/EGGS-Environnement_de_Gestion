from django.contrib.auth.models import User
import re


def check_password_condition(password) -> bool:
    if len(password) < 8:  # au moins 8 caractères
        return False

    elif not re.findall('[A-Z]', password):  # s'il contient pas au moins une majuscules
        return False

    elif not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
        return False

    elif not re.findall('[0-9]{2}', password):
        return False

    return True

"""
def check_error_userForm(password, password_confirmation, username, email) -> str:
    # Vérification si le nom d'utilisateur n'est pas déjà existant
    if User.objects.filter(username=username).exists():
        return "username"

    # Vérification si l'email n'est pas déjà existant
    elif User.objects.filter(email=email).exists():
        return "email"

    # Vérification de la confirmation du mot de passe
    elif password != password_confirmation:
        return "different_password"

    elif not check_password_condition(password):
        return "password_condition"

    return "None"
"""
