from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, "manager/dashboard.html")


@login_required
def contact(request):
    return render(request, "manager/contact.html")


