from django.db import models

# Create your models here.
# models.py

class Device(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()

class Sensor(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    sensor_type = models.CharField(max_length=50)
    value = models.FloatField()

    def __str__(self):
        return f"{self.sensor_type} - {self.value} at {self.timestamp}"