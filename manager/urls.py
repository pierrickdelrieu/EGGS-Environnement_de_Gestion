from django.urls import path
from . import views

app_name = "manager"
urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('contact/', views.contact, name="contact"),
    path('add_database/', views.add_database, name="add_database"),
    path('add_product/', views.add_product, name="add_product"),
    path('details_product/(?P<product_id>[0-9]+)/', views.details_product, name='details_product'),
    path('update_product/(?P<product_id>[0-9]+)/', views.update_product, name="update_product"),
    path('display_products/', views.display_products, name="display_products"),
    path('switch_current_db/(?P<database_name>[0-9]+)/', views.switch_current_db, name="switch_current_db"),
    path('my_databases/', views.my_databases, name="my_databases"),
]