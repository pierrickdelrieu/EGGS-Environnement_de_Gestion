from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from home.models import DataBase

from django.contrib.auth import get_user_model

User = get_user_model()  # new User definitions


class ContactForm(forms.Form):
    subject = forms.CharField(label="Object", max_length=100, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Objet"}))
    message = forms.CharField(label="Message", max_length=1200, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Message"}))


class AddDbForm(forms.Form):
    name = forms.CharField(label="Nom", max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Name"}))
    type = forms.CharField(label="Catégorie", max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Type"}))
    user = None

    def __init__(self, *args, **kwargs):
        super(AddDbForm, self).__init__(*args, **kwargs)
        initial = kwargs.pop('initial')
        self.user = initial['user']

    def clean_name(self):
        user = User.objects.get(username=self.user.username)
        name = self.cleaned_data.get("name") + ' (' + user.first_name[0].upper() + \
               user.last_name[0].upper() + user.last_name[len(user.last_name) - 1].upper() + ')'
        if name and DataBase.objects.filter(name=name).exists():
            raise ValidationError(
                _("Le nom de la base de donnéee n'est pas disponible"),
                code='db_exist',
            )
        return name


class AddProductForm(forms.Form):
    name = forms.CharField(label="Nom", max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Nom"}))
    quantity = forms.IntegerField(label="Quantité", required=True, widget=forms.TextInput(
        attrs={'placeholder': "Quantité"}))
    price = forms.IntegerField(label="Prix", required=True, widget=forms.TextInput(
        attrs={'placeholder': "Prix"}))
    user = None

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        initial = kwargs.pop('initial')
        self.user = initial['user']

    def clean_name(self):
        name = self.cleaned_data.get("name")
        user = User.objects.get(username=self.user.username)
        if name and user.current_database.products.filter(name=name).exists():
            raise ValidationError(
                _("Vous avez déjà un produit dans cette base de donnée avec le même nom"),
                code='product_exist',
            )
        return name

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        if quantity and quantity < 0:
            raise ValidationError(
                _("La quantité doit être positive ou nul"),
                code='quantity_is_negative',
            )
        return quantity

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price and price < 0:
            raise ValidationError(
                _("Le price doit être positif ou nul"),
                code='price_is_negative',
            )
        return price
