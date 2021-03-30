from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


def connexion(request):
    error = False

    if request.user.is_authenticated:
        return HttpResponseRedirect('/manager/')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # vérifications si les données sont corrects
            if user:  # si user ≠ None
                login(request, user)
                return HttpResponseRedirect('/manager/')
            else:
                error = True
    else:
        form = LoginForm()

    return render(request, 'home/login.html', locals())


def inscription(request):
    error = False
    error_username = False
    error_password = False

    if request.user.is_authenticated:
        return HttpResponseRedirect('/manager/')
    elif request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            # Vérification si le nom d'utilisateur n'est pas déjà existant
            if User.objects.filter(username=username).exists():
                error_username = True
                new_user = None
            # Vérification de la confirmation du mot de passe
            elif password1 != password2:
                error_password = True
                new_user = None
            else:
                new_user = User.objects.create_user(username, email, password1)

            if new_user:  # si user ≠ None
                user = UserManager(userModel=new_user)
                user.save()
            else:
                error = True
    else:
        form = SigninForm()

    return render(request, 'home/signin.html', locals())


def pwdRecovery(request):
    form = PwdRecoveryForm()
    return render(request, 'home/pwdRecovery.html', locals())


def deconnexion(request):
    logout(request)
    return HttpResponseRedirect('/home/login/')
