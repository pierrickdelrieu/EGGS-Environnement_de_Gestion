from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


def connexion(request):
    error = False

    if request.user.is_authenticated:
        return HttpResponseRedirect('/manager/')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.log(request):
                return HttpResponseRedirect('/manager/')
            else:
                error = True
    else:
        form = LoginForm()

    return render(request, 'home/login.html', locals())


def inscription(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/manager/')
    elif request.method == 'POST':
        form = SigninForm(request.POST)

        if form.is_valid():
            error = form.check_error()

            if error == "None":
                form.signup()
                return HttpResponseRedirect('/home/login/')

    else:
        form = SigninForm()

    return render(request, 'home/signin.html', locals())


def deconnexion(request):
    logout(request)
    return HttpResponseRedirect('/home/login/')
