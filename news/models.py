from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    time=models.DateTimeField()
    image = models.CharField(max_length=255, null=True)
