from django.urls import path
from .views import home, ProductView, CategoryView

urlpatterns = [
    path('', home, name='home-view'),
    path('product/', ProductView.as_view(), name='products-list'),
    path('product/<int:pk>/', ProductView.as_view(), name='product-view'),
    path('product/category/<str:category>/', ProductView.as_view(), name='products-by-category'),
    path('product/category/', CategoryView.as_view(), name='category-list'),
]
