from django.db import models
from movies.models import Movie
from studios.models import Studio
import uuid
 
# Create your models here.
class Showtime(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
 
    class Meta:
        db_table = 'showtimes'
        unique_together = ('movie', 'studio', 'start_time')
 
    def __str__(self):
        return f'{self.movie.name} at {self.studio.name}'