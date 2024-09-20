from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, DestroyModelMixin
from product.models import Product
from .models import Order, OrderItem
from .serializer import OrderSerializer, OrderItemSerializer


class OrderListAPIView(GenericAPIView, ListModelMixin, DestroyModelMixin, UpdateModelMixin):
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        queryset = Order.objects.filter(user_id=request.user.id)
        if queryset.exists():
            self.queryset = queryset
            return self.list(request, *args, **kwargs)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        self.queryset = Order.objects.get(user_id=request.user.id, status=True)
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        self.queryset = Order.objects.get(user_id=request.user.id, status=True)
        return self.update(request, *args, **kwargs)
    

class OrderItemAPIView(APIView):

    def post(self, request, *args, **kwargs):
        item = Product.objects.get(pk=kwargs['pk'])
        quantity = int(request.data.get('quantity', 1))
        total_price = int(request.data.get('price', 0)) * quantity
        order = Order.objects.filter(user_id=request.user.id, status=True)
        if not order.exists():
            order = Order.objects.create(user_id=request.user.id)
            order.status = True
            order.save()

        else:
            order = order[0]

        order_item = OrderItem.objects.create(order=order, item=item, quantity=quantity, total_price=total_price)
        serializer = OrderItemSerializer(order_item)
        item.quantity -= quantity
        item.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        OrderItem.objects.get(pk=kwargs['pk']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)