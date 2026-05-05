from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Product
    fields = ['id', 'name', 'sku', 'description', 'shop', 'location', 'price', 'discount', 'category', 'stock', 'is_available', 'picture', 'is_delete']