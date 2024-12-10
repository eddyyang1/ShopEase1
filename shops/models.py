# shops/models.py

from django.db import models
from users.models import CustomUser

class Shop(models.Model):
    name = models.CharField(max_length=200)
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='shop')
    description = models.TextField()
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name