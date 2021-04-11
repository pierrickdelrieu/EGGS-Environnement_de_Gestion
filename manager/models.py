from django.db import models
from home.models import Manager


# Create your models here.


class Product(models.Model):
    quantity = models.IntegerField("Quantité")
    price = models.IntegerField("Prix")
    description = models.CharField("Description", max_length=200)

    def create(self, quantity: quantity, price: price, description: description):
        self.quantity = quantity
        self.price = price
        self.description = description


class DataBase(models.Model):
    type = models.CharField("Catégorie", max_length=50)
    description = models.CharField("Description", max_length=200)


    def create(self, type: type, description: description):
        self.type = type
        self.description = description
