from django.urls import path
from . import views

app_name = "manager"
urlpatterns =[
    path('', views.manager, name="manager"),
    path('contact/', views.contact, name="contact"),
]
