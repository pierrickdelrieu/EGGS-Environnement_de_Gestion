from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.contrib.auth import get_user_model

User = get_user_model()  # new User definitions


@login_required
def dashboard(request):
    return render(request, "manager/dashboard.html")


@login_required
def contact(request):
    send = False
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = "Contact - " + form.cleaned_data.get('subject')
            user = User.objects.get(username=request.user.username)
            message = "Utilisateur : " + user.get_full_name() + " " + user.email + '\n\n' \
                      + form.cleaned_data.get('message')

            send_mail(subject=subject, message=message, from_email=None, recipient_list=['eggs.contacts@gmail.com'])
            send = True

    form = ContactForm()  # Réintialisation du formulaire

    return render(request, "manager/contact.html", locals())


@login_required
def add_database(request):
    user = request.user

    if request.method == 'POST':
        form = AddDbForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get("name")
            type = form.cleaned_data.get("type")
            user = request.user

            db = DataBase()
            db.create(name=name, type=type)
            db.save()
            db.add_owner(user)
            user.update_current_database(db)

    form = AddDbForm()  # Réintialisation du formulaire

    return render(request, "manager/add_db.html", locals())


@login_required
def add_product(request):
    user = request.user
    current_database = user.current_database

    if current_database is not None:
        if user.is_owner(current_database) or user.is_editor(current_database):
            if request.method == 'POST':
                form = AddProductForm(request.POST)

                if form.is_valid():
                    name = form.cleaned_data.get("name")
                    quantity = form.cleaned_data.get("quantity")
                    price = form.cleaned_data.get("price")

                    product = Product()
                    product.create(name=name, quantity=quantity, price=price, database=current_database)
                    product.save()

            form = AddProductForm()  # Réintialisation du formulaire

        else:
            return HttpResponseRedirect('/manager/dashboard/')
    else:
        return HttpResponseRedirect('/manager/add_database/')

    return render(request, "manager/add_products.html", locals())
