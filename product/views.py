from .models import Product, ProductCategory
from .serializer import ProductSerializer, ProductCategorySerializer
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
            self.queryset = Product.objects.filter(category__name=kwargs['category'])
            return render(request, 'category.html', {'data': self.list(request).data})

        return self.list(request)

    def post(self, request):
        ...

    def put(self, request, product_id):
        ...

    def delete(self, request, product_id):
        ...


class CategoryView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   generics.GenericAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request):
        ...

    def put(self, request, product_id):
        ...

    def delete(self, request, product_id):
        ...
