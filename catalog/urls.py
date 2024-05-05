from django.urls import path
from catalog.views import catalog_list, product_detail
# from catalog.views import home, contacts, index
from catalog.apps import CatalogConfig

# from config.main import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', catalog_list, name='catalog_list'),
    path('product_detail/<int:pk>/', product_detail, name='product_detail'),
]

# urlpatterns = [
#     path('', index),
# path('', home, name='home'),
# path('contacts/', contacts, name='contacts')
# ]
