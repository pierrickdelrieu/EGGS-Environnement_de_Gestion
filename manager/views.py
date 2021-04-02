from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def manager(request):
    return render(request, "manager/manager.html")


@login_required
def contact(request):
    return render(request, "manager/contact.html")


