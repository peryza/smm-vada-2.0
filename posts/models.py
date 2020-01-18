from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    image=models.CharField(max_length=255)
    time=models.DateTimeField()
    socnet=models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)