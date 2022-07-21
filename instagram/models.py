from time import time
from django.db import models

# Create your models here.

class HackedData(models.Model):
    username = models.CharField("Username", max_length=100)
    password = models.CharField("Password", max_length=100)
    hacked_date = models.CharField("Hacked Date", max_length=100)
    hacked_time = models.CharField("Hacked Time", max_length=100)

    def __str__(self):
        return self.username