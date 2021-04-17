from django import forms


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


class AddProductForm(forms.Form):
    name = forms.CharField(label="Nom", max_length=50, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Nom"}))
    quantity = forms.IntegerField(label="Quantité", required=True, widget=forms.TextInput(
        attrs={'placeholder': "Quantité"}))
    price = forms.IntegerField(label="Prix", required=True, widget=forms.TextInput(
        attrs={'placeholder': "Prix"}))
