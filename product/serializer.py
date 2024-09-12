from rest_framework import serializers
from .models import Product, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id',
                  'name',
                  'description',
                  'price',
                  'quantity',
                  'category',
                  'images']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['alt',
                  'image']
