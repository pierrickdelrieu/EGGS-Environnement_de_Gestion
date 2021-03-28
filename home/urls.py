from django.urls import path
from . import views

app_name = "home"
urlpatterns =[
    path('signin/', views.signin, name="signin"),
    path('login/', views.login, name="login"),
    path('pwdRecovery/', views.pwdRecovery, name="pwdRecovery"),
]
