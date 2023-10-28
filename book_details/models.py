from django.db import models
from django.contrib.auth.models import User
from landingPage.models import Books

class discussion(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, default='')
    comment = models.CharField(max_length=500)
    user = models.CharField(max_length=255,default='')

class reply(models.Model):
    comment = models.ForeignKey(discussion, on_delete=models.DO_NOTHING, default='')
    replies = models.CharField(max_length=255, default='')
    user = models.CharField(max_length=255,default='')
