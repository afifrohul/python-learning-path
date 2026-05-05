from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  name = models.CharField(max_length=50)
  sku = models.CharField(max_length=10)
  description = models.TextField()
  shop = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  price = models.IntegerField()
  discount = models.IntegerField()
  category = models.CharField(max_length=50)
  stock = models.IntegerField()
  is_available = models.BooleanField()
  picture = models.TextField()
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)
  is_delete = models.BooleanField(default=False)