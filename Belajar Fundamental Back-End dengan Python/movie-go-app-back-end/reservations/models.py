from django.db import models
from django.contrib.auth.models import User
from seats.models import Seat
from showtimes.models import Showtime
import uuid
 
# Create your models here.
class Reservation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    amount = models.IntegerField()
    reserved_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.user.username} - {self.showtime}'
 
    class Meta:
        db_table = 'reservations'
 
class ReservedSeat(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
 
    class Meta:
        unique_together = ('seat', 'showtime', 'reservation')