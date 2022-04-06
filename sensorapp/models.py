from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Device(models.Model):

  sensor_id = models.CharField(max_length=12, null=True)
  sensor_type = models.CharField(max_length=22,null=True)
  value = models.DecimalField(max_digits = 5,decimal_places = 2)
  unit = models.CharField(max_length=22, null=True)
  timestamp = models.DateTimeField()
  # timestamp = models.IntegerField(default=int(datetime.now().timestamp()), blank=True, null=True)
  location = models.CharField(max_length=12, null=True)