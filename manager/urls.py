from django.urls import path
from . import views

app_name = "manager"
urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('contact/', views.contact, name="contact"),
    path('add_database/', views.add_database, name="add_database"),
    path('add_product/', views.add_product, name="add_product"),
    path('details_product/(?P<product_id>[0-9]+)/', views.details_product, name='details_product'),
    path('display_products/', views.display_products, name="display_products"),
]