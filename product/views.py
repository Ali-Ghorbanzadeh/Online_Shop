from .models import Product, ProductImage
from .serializer import ProductSerializer, ProductImageSerializer
from rest_framework import mixins
from rest_framework import generics
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


class ProductView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)

        elif 'category' in kwargs:
            self.__class__.queryset = Product.objects.filter(category__name=kwargs['category'])
            return self.list(request, *args, **kwargs)

        return self.list(request)

    def post(self, request):
        ...

    def put(self, request, product_id):
        ...

    def delete(self, request, product_id):
        ...


class ProductImageView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       generics.GenericAPIView):

    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request)

    def post(self, request):
        ...

    def put(self, request, product_id):
        ...

    def delete(self, request, product_id):
        ...
