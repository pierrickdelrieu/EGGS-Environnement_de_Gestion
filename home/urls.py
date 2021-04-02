from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .forms import PasswordResetConfirmationForm, PasswordResetFormEmail

app_name = "home"
urlpatterns = [
    path('signin/', views.inscription, name="signin"),
    path('login/', views.connexion, name="login"),
    path('logout/', views.deconnexion, name="logout"),

    # URL de réinitialisation de mot de passe par mail
    # Utilisation de views deja existante dans la bibliothèques 'django.contrib.auth'
    # cf. documentation : https://docs.djangoproject.com/fr/3.1/topics/auth/default/
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='home/password_reset.html',
                                                                 email_template_name='home/password_reset_email.html',
                                                                 subject_template_name='home/password_reset_subject.txt',
                                                                 success_url=reverse_lazy('home:password_reset_done'),
                                                                 form_class=PasswordResetFormEmail),
         name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="home/password_reset_done.html"),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="home/password_reset_confirm.html",
                                                     success_url=reverse_lazy('home:password_reset_complete'),
                                                     form_class=PasswordResetConfirmationForm),
         name='password_reset_confirm'),

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="home/password_reset_complete.html"),
         name='password_reset_complete'),
]
