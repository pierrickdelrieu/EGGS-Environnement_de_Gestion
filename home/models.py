from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# https://github.com/django/django/blob/main/django/contrib/auth/models.py
class Manager(AbstractUser):
    email = models.EmailField(_('Adresse email'), unique=True, blank=False)
    first_name = models.CharField(_('Prénom'), max_length=150, blank=False)
    last_name = models.CharField(_('Nom'), max_length=150, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def create_user(self, first_name, last_name, email, password):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email.lower()
        self.set_password(password)

    def set_username(self):
        self.save()  # To have an id the user must be saved in the database
        self.username = self.first_name.lower() + self.last_name.lower() + str(self.id)
        self.save()







