from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(label="Object", max_length=100, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Objet"}))
    message = forms.CharField(label="Message", max_length=1200, required=True, widget=forms.TextInput(
        attrs={'placeholder': "Message"}))
