from django.db import models

# Create your models here.
class sport(models.Model):
    idk = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    photo = models.CharField(max_length=49)
    desc = models.TextField()
