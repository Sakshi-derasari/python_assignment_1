from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomeUserManager

class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CustomeUser(AbstractUser):
    username = None

    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=15, unique=True)
    bio = models.TextField(blank=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = CustomeUserManager()

    def __str__(self):
        return self.phone