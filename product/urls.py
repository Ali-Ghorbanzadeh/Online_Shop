from django.urls import path
from .views import ProductView, home, ProductImageView

urlpatterns = [
    path('', home, name='home-view'),
    path('product/', ProductView.as_view(), name='products-list'),
    path('product/<int:pk>/', ProductView.as_view(), name='product-view'),
    path('product/<str:category>/', ProductView.as_view(), name='products-by-category'),
    path('product/image/<int:pk>/', ProductImageView.as_view(), name='product-image'),
]
