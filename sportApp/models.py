from django.db import models

# Create your models here.
class sport(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()


class user(models.Model):
    tabnum = models.CharField(max_length=6)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

class type1(models.Model):
    contacts = models.CharField(max_length=20)
    desc = models.TextField()
    user = models.OneToOneField(user, on_delete = models.CASCADE, primary_key = True)

class type2(models.Model):
    email = models.CharField(max_length=30)
    group = models.CharField(max_length=7)
    goal = models.CharField(max_length=3)
    user = models.OneToOneField(user, on_delete = models.CASCADE, primary_key = True)

class place(models.Model):
    name = models.CharField(max_length=50)


class lesson(models.Model):
    sport = models.ForeignKey(sport, on_delete = models.CASCADE)
    coach = models.ForeignKey(type1, on_delete = models.DO_NOTHING)
    lvl = models.CharField(max_length=1)
    wday = models.CharField(max_length=13)
    tday = models.CharField(max_length=5)
    place = models.ForeignKey(place, on_delete = models.PROTECT)
    stud = models.ManyToManyField(type2)
    countmax = models.CharField(max_length=4)
    countnow = models.CharField(max_length=4)

class messages(models.Model):
    time = models.CharField(max_length=20)
    message = models.TextField()
    lesson = models.ForeignKey(lesson, on_delete = models.CASCADE)
