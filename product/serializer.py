from rest_framework import serializers
from .models import Product, ProductImage, ProductCategory


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['alt',
                  'image']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id',
                  'name',
                  'description',
                  'price',
                  'quantity',
                  'category',
                  'images']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id',
                  'name']
