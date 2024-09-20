from .models import Product, ProductCategory
from .serializer import ProductSerializer, ProductCategorySerializer
from rest_framework import mixins, generics
from rest_framework.viewsets import ViewSet
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# def home(request):
#     return render(request, 'home.html')


class HomeView(ListView):
    model = Product
    template_name = 'home.html'


class ProductView(mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):

        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)

        elif 'category' in kwargs:
            self.queryset = Product.objects.filter(category__name=kwargs['category'])
            return render(request, 'category.html', {'data': self.list(request).data})

        return self.list(request)


class CategoryView(mixins.ListModelMixin, generics.GenericAPIView, mixins.DestroyModelMixin):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)
