from django.db import models
from datetime import datetime


class Foreman(models.Model):
    """Docstring for Foreman."""
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    email = models.EmailField(max_length=50)
    is_our = models.BooleanField(default=True)
    hire_date = models.DateTimeField(default=datetime, blank=True)

    def __str__(self):
        return self.name
