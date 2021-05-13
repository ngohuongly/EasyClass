from django.db import models
from django.urls import reverse

class Event(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

# Create your models here.
