from django.db import models
import uuid
from core.models import User
from tickets.models import Ticket

# Create your models here.
class Registration(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'registrations'