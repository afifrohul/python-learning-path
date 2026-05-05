from django.db import models
from studios.models import Studio
import uuid
 
# Create your models here.
class Seat(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
 
    class Meta:
        db_table = 'seats'
        unique_together = ('studio', 'seat_number')
 
    def __str__(self):
        return f'{self.studio.name} - {self.seat_number}'