from django.db import models

# Create your models here.
class sport(models.Model):
    idKey = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    photo = models.ImageField()
    Desc = models.TextField()
