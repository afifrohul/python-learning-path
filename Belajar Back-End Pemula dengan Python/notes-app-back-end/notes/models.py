from django.db import models

# Create your models here.
import uuid

class Note(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  title = models.CharField(max_length=30)
  body = models.TextField()
  tags = models.JSONField()
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)