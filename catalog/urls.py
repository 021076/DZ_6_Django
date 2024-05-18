from django.urls import path
from catalog.views import ProductListView, ProductDetailView, contacts
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('', ProductListView.as_view(), name='catalog_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
