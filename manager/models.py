from django.db import models
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from home.models import Manager


class DataBase(models.Model):
    name = models.CharField("Nom", max_length=50, default="Inconnu")
    type = models.CharField("Catégorie", max_length=50, default="Inconnu")

    def create(self, name: str, type: str):
        self.name = name
        self.type = type

    def add_owner(self, user: 'Manager'):
        user.owner.add(self)
        self.save()

    def add_editor(self, user: 'Manager'):
        user.editor.add(self)
        self.save()

    def add_reader(self, user: 'Manager'):
        user.reader.add(self)
        self.save()


class Product(models.Model):
    name = models.CharField("Nom", max_length=50, default="Inconnu")
    quantity = models.IntegerField("Quantité", default=0)
    price = models.IntegerField("Prix", default=0)

    database = models.ForeignKey(DataBase, on_delete=models.CASCADE, related_name='products', null=True)

    def create(self, name: str, quantity: int, price: int, database: DataBase):
        self.name = name
        self.quantity = quantity
        self.price = price

        # Ajout du produit dans la base de donnée
        # bulk=False permet d'eviter les erreurs lors de l'ajout du produit sur l'enregistrement du produit dans la BDD
        database.products.add(self, bulk=False)
