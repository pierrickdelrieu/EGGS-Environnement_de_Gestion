from django.db import models
from home.models import Manager


# Create your models here.

class Product(models.Model):
    name = models.CharField("Nom", max_length=50, default="Inconnu")
    quantity = models.IntegerField("Quantité", default=0)
    price = models.IntegerField("Prix", default=0)

    def create(self, name: name, quantity: quantity, price: price):
        self.name = name
        self.quantity = quantity
        self.price = price


class DataBase(models.Model):
    name = models.CharField("Nom", max_length=50, default="Inconnu")
    type = models.CharField("Catégorie", max_length=50, default="Inconnu")

    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='databases', blank=True)

    def create(self, name: name, type: type):
        self.name = name
        self.type = type