from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

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
        name = self.cleaned_data.get("name")
        user = User.objects.get(username=self.user.username)
        if name and (user.owner.filter(name=name).exists() or
                     user.editor.filter(name=name).exists() or
                     user.reader.filter(name=name).exists()):
            raise ValidationError(
                _("Vous avez déjà une base de donnée avec le même nom"),
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
