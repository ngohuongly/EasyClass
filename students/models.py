from django.db import models
from django.forms import ModelForm

class studentsinformation(models.Model):
    Name=models.CharField(max_length=100)
    Emails=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Parents_name=models.CharField(max_length=100)
    Parents_emails=models.CharField(max_length=100)
    Phone=models.CharField(max_length=100)

class studentsForm(ModelForm):
    class Meta:
        model = studentsinformation
        fields = ['Name','Emails','Address','Phone']# Create your models here.
