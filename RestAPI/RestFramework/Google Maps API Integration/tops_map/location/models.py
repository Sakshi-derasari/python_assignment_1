from django.db import models

class InstituteLocation(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.city}"