from django.db import models
from django.forms import ModelForm

# Create your models here.
class Classes(models.Model):
    Class_ID = models.CharField(max_length=64)
    Title = models.CharField(max_length=255, unique=True)
    Desc = models.TextField()
    Teacher_name = models.CharField(max_length = 64)
    Teaching_assistant_name = models.CharField(max_length = 64)
    Schedule = models.DateField()
    Prerequisite = models.TextField()
    Max_number_of_students = models.CharField(max_length=2)
    Permanent_zoom_meeting_links=models.URLField(max_length=200)

class Classes_Desc(models.Model):
    Class_ID = models.CharField(max_length=64)
    Title = models.CharField(max_length=255, unique=True)
    Desc = models.TextField()
    Teacher_name = models.CharField(max_length = 64)
    Teaching_assistant_name = models.CharField(max_length = 64)
    Schedule = models.DateField()
    Prerequisite = models.TextField()
    Max_number_of_students = models.CharField(max_length=2)
    Permanent_zoom_meeting_links=models.URLField(max_length=200)


class Submission(models.Model):
    Class_ID = models.CharField(max_length=64)
    Student_name = models.CharField(max_length=64)
    Student_ID = models.CharField(max_length=64)
    Note = models.TextField()
    Github_page=models.URLField(max_length=200)
    File_upload=models.FileField()

class submissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['Class_ID','Student_name','Student_ID','Note','Github_page','File_upload']
