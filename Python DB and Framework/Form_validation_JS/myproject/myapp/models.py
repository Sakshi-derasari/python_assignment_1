from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phoneno = models.CharField(max_length=10)

    def __str__(self):
        return self.name