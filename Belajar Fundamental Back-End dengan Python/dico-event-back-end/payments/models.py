from django.db import models
import uuid
from registrations.models import Registration

# Create your models here.
class Payment(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
  payment_method = models.CharField(max_length=50)
  payment_status = models.CharField(max_length=50)
  amount_paid = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'payments'