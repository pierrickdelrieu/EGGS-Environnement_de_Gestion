from django.shortcuts import render


def login(request):
    return render(request, 'home/login.html')


def signin(request):
    return render(request, 'home/signin.html')


def pwdRecovery(request):
    return render(request, 'home/pwdRecovery.html')