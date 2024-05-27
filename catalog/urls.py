from django.urls import path

from blog.views import PostCreateView, PostUpdateView, PostDeleteView
from catalog.views import ProductListView, ProductDetailView, contacts, ProductDeleteView, ProductUpdateView, \
    ProductCreateView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    # path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_create/', ProductCreateView.as_view(), name="product_create"),
    path('product_form/<int:pk>/', ProductUpdateView.as_view(), name="product_edit"),
    path('product_confirm_delete/<int:pk>/', ProductDeleteView.as_view(), name="product_delete"),
]
