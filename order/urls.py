from django.urls import path
from .views import OrderListAPIView, OrderItemAPIView

urlpatterns = [
    path('api/order/', OrderListAPIView.as_view(), name='order-list'),
    path('api/order-item/<int:pk>/', OrderItemAPIView.as_view(), name='order-item-view'),
]