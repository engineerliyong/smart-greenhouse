from django.db import models

class SensorReading(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    light = models.IntegerField()
    soil = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at} - {self.temperature}°C"