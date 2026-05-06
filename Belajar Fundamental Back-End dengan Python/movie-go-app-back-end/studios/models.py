from django.db import models
from core.models import User
import uuid
 
# Create your models here.
class Studio(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    seat_capacity = models.IntegerField()
 
    def __str__(self):
        return self.name
 
    class Meta:
        db_table = 'studios'
 
class StudioManager(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
 
    class Meta:
        db_table = 'studio_managers'