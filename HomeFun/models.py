from django.db import models

class Experiments(models.Model):
    Title = models.CharField(max_length=255, unique=True)
    Desc = models.TextField()
    Preparation = models.TextField()
    How_to_do = models.TextField()
#    def __str__(self):
#        return self.Title
