from django.db import models
import uuid
 
# Create your models here.
class Movie(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField()
    country = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    producer = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    duration = models.IntegerField()
    genre = models.CharField(max_length=100)
 
    def __str__(self):
        return self.name
 
    class Meta:
        db_table = 'movies'