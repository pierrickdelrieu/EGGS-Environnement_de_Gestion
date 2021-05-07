from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from manager.models import DataBase


# https://github.com/django/django/blob/main/django/contrib/auth/models.py
class Manager(AbstractUser):
    email = models.EmailField(_('Adresse email'), unique=True, blank=False)
    first_name = models.CharField(_('Prénom'), max_length=150, blank=False)
    last_name = models.CharField(_('Nom'), max_length=150, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    current_database = models.ForeignKey(DataBase, on_delete=models.CASCADE, related_name='current_user', null=True)

    owner = models.ManyToManyField(DataBase, related_name='user_owner', null=True)
    editor = models.ManyToManyField(DataBase, related_name='user_editor', null=True)
    reader = models.ManyToManyField(DataBase, related_name='user_reader', null=True)

    def set(self, first_name, last_name, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email.lower()

    def set_username(self):
        self.save()  # To have an id the user must be saved in the database
        self.username = self.first_name.lower() + self.last_name.lower() + str(self.id)
        self.save()

    def update_current_database(self, database: DataBase):
        if database is not None:
            if self.has_role_in_db(database=database):
                self.current_database = database
                self.save()

    def is_owner(self, database: DataBase) -> bool:
        if self in database.user_owner.all():
            return True
        return False

    def is_editor(self, database: DataBase) -> bool:
        if self in database.user_editor.all():
            return True
        return False

    def is_reader(self, database: DataBase) -> bool:
        if self in database.user_reader.all():
            return True
        return False

    def is_current_owner(self) -> bool:
        if self.current_database is not None:
            if self in self.current_database.user_owner.all():
                return True
        return False

    def is_current_editor(self) -> bool:
        if self.current_database is not None:
            if self in self.current_database.user_editor.all():
                return True
        return False

    def is_current_reader(self) -> bool:
        if self.current_database is not None:
            if self in self.current_database.user_reader.all():
                return True
        return False

    def count_database(self) -> int:
        return self.owner.count() + self.editor.count() + self.reader.count()

    def has_role_in_db(self, database: DataBase):
        return self.is_owner(database) or self.is_editor(database) or self.is_reader(database)
