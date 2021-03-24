from django.db import models

class notif(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    notif_time=models.DateTimeField()
    Classification=models.CharField(
        max_length=10,
        choices=[
            ('Important',"Important"),
            ('URGENT', "Urgent"),
            ('FYI',"For Your Information"),
        ]
    )
