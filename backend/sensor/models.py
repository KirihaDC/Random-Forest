from django.db import models

class SensorData(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
