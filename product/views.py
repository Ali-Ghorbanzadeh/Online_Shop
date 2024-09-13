from .models import Product, ProductImage, ProductCategory
from .serializer import ProductSerializer, ProductImageSerializer, ProductCategorySerializer
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
            data = [{'details': product,
                     'image': ProductImage.objects.filter(product_id=product.id)} for product in Product.objects.filter(category__name=kwargs['category'])]
            return render(request, 'category.html', {'data': data})

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
