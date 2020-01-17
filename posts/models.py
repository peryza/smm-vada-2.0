from django.db import models
from django.conf import settings


class Network(models.Model):
    name=models.CharField(max_length=255)

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    image=models.CharField(max_length=255)
    time=models.DateTimeField()
    socnet=models.ForeignKey('Network', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)