from django.db import models
import uuid
from core.models import User

# Create your models here.
class Event(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  organizer = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.TextField()
  location = models.CharField(max_length=100)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  status = models.CharField(max_length=50)
  quota = models.IntegerField()
  category = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'events'
  
  def __str__(self):
    return f'{self.events.name}'
  
