from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render
from .forms import SigninForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

from django.contrib.auth import get_user_model

User = get_user_model()  # new User definitions


def about(request):
    return render(request, 'home/about.html', locals())


def connexion(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/manager/dashboard/')

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():  # If there is no error (clean) in the form
            email = form.cleaned_data.get('email').lower()
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)  # vérifications si les données sont corrects
            login(request, user)
            return HttpResponseRedirect('/manager/dashboard/')
    else:
        form = LoginForm()

    return render(request, 'home/login.html', locals())


def inscription(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/manager/dashboard/')

    elif request.method == 'POST':
        form = SigninForm(request.POST)

        if form.is_valid():  # If there is no error (clean) in the form
            user = form.save(commit=False)  # User registration but not in the database
            user.is_active = False  # Blocking user login

            user.save()  # User registration in the database
            user.set_username()  # Initializing username

            # envoie du mail de confirmation
            current_site = get_current_site(request)
            mail_subject = 'Active ton compte EGGS'
            message = render_to_string('home/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data['email'].lower()
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()

            return HttpResponseRedirect('/home/activate_done/')
    else:
        form = SigninForm()

    return render(request, 'home/signin.html', locals())


def deconnexion(request):
    logout(request)
    return HttpResponseRedirect('/')


# cf : https://medium.com/@frfahim/django-registration-with-confirmation-email-bb5da011e4ef
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True  # Activate the possibility of connection
        user.save()  # User registration in the database
        login(request, user)
        return HttpResponseRedirect('/manager/dashboard/')
    else:
        return HttpResponse("Lien d'activation invalide")


def activate_done(request):
    return render(request, 'home/acc_active_done.html', locals())

