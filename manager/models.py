from django.db import models
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from home.models import Manager


class DataBase(models.Model):
    name = models.CharField("Nom", max_length=50, default="Inconnu")
    type = models.CharField("Catégorie", max_length=50, default="Inconnu")

    def set(self, name: str, type: str):
        self.name = name
        self.type = type

    def add_owner(self, user: 'Manager'):
        self.user_owner.add(user)
        self.save()
        if user.current_database is None:
            user.update_current_database(self)

    def add_editor(self, user: 'Manager'):
        self.user_editor.add(user)
        self.save()
        if user.current_database is None:
            user.update_current_database(self)

    def add_reader(self, user: 'Manager'):
        self.user_reader.add(user)
        self.save()
        if user.current_database is None:
            user.update_current_database(self)


class Product(models.Model):
    name = models.CharField("Nom", max_length=50, default="Inconnu")
    quantity = models.IntegerField("Quantité", default=0)
    price = models.IntegerField("Prix", default=0)

    database = models.ForeignKey(DataBase, on_delete=models.CASCADE, related_name='products', null=True)

    def set(self, name: str, quantity: int, price: int):
        self.name = name
        self.quantity = quantity
        self.price = price
