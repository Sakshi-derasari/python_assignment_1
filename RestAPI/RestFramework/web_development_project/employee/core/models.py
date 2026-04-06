from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name