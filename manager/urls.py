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
    path('compte/', views.compte, name="compte"),
    path('update_compte/', views.update_compte, name="update_compte"),
    path('update_password/', views.update_password, name="update_password"),
    path('settings_database/', views.settings_database, name="settings_database"),

    path('add_owner_db/', views.add_owner_db, name="add_owner_db"),
    path('add_editor_db/', views.add_editor_db, name="add_editor_db"),
    path('add_reader_db/', views.add_reader_db, name="add_reader_db"),

    path('leave_db/', views.leave_db, name="leave_db"),
    path('delete_editor_db/(?P<username>[0-9]+)/', views.delete_editor_db, name="delete_editor_db"),
    path('delete_reader_db/(?P<username>[0-9]+)/', views.delete_reader_db, name="delete_reader_db"),

    path('delete_product/(?P<product_id>[0-9]+)/', views.delete_product, name="delete_product"),
    path('delete_database/', views.delete_database, name="delete_database"),


]