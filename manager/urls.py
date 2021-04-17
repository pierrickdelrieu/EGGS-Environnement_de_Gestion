from django.urls import path
from . import views

app_name = "manager"
urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('contact/', views.contact, name="contact"),
    path('add_database/', views.add_database, name="add_database"),
    path('add_product/', views.add_product, name="add_product"),
]
