from django.db import models

class Pamf(models.Model):
    """
    Represents an ESP32 device 
    """
    name = models.CharField(max_length=100)
    device_id = models.CharField(max_length=100, unique=True)   # helps specify the units
    last_seen = models.DateTimeField(auto_now=True)  # Timestamp of last communication
    
    def __str__(self):
        return self.name

class Command(models.Model):
    """
    Represents a command sent to the ESP32
    """
    device = models.ForeignKey(Pamf, on_delete=models.CASCADE)
    command_type = models.CharField(max_length=50)  # e.g., 'start', 'stop', 'update'
    command_data = models.JSONField()  # Stores command parameters in JSON format
    timestamp = models.DateTimeField(auto_now_add=True)  # When the command was issued

    def __str__(self):
        return f"Command to {self.device.name} - {self.command_type}"

class SensorData(models.Model):
    """
    Represents data received from the ESP32
    """
    device = models.ForeignKey(Pamf, on_delete=models.CASCADE)
    data_type = models.CharField(max_length=50)  # e.g., 'temperature', 'humidity'
    data_value = models.FloatField()  # The actual sensor value
    timestamp = models.DateTimeField(auto_now_add=True)  # When the data was received

    def __str__(self):
        return f"{self.data_type} from {self.device.name} at {self.timestamp}"