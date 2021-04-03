from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Manager(AbstractUser):
    email = models.EmailField(_('Adresse email'), unique=True, blank=False)
    first_name = models.CharField(_('Prénom'), max_length=150, blank=False)
    last_name = models.CharField(_('Nom'), max_length=150, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # https://github.com/django/django/blob/main/django/contrib/auth/models.py
    def create_user(self, first_name, last_name, email, password):
        self.save()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = first_name.lower() + last_name.lower() + str(self.id)
        self.email = email.lower()
        self.set_password(password)
        self.save()




