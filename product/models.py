from django.db import models
from core.models import AbstractModel


class ProductCategory(AbstractModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(AbstractModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(null=True, blank=True, default=0)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING, related_name='category')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductImage(AbstractModel):
    alt = models.CharField(max_length=100, null=True, blank=True, default='Unknown Image')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='images')
    image = models.ImageField(upload_to='product/images/', null=True, blank=True)

    def __str__(self):
        return self.image.url
