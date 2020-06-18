from django.db import models


# Create your models here.
class Data(models.Model):
    mid = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1280)