from django.db import models

class SensorData(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"x={self.x}, y={self.y}, z={self.z} at {self.timestamp}"