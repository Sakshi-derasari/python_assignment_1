from django.db import models

# Create your models here.

class Professional(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    speciality = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.username