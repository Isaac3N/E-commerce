from django.urls import path
from .views import get_routes, get_products, get_product

urlpatterns = [
    path('', get_routes, name='routes'),
    path('products', get_products, name='products'),
    path('products/<str:pk>', get_product, name='product'),
]
