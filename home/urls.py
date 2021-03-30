from django.urls import path
from . import views

app_name = "home"
urlpatterns =[
    path('signin/', views.inscription, name="signin"),
    path('login/', views.connexion, name="login"),
    path('pwdRecovery/', views.pwdRecovery, name="pwdRecovery"),
]
