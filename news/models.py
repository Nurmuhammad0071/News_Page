from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    eamil = models.EmailField(max_length=250)
    age = models.IntegerField()


class News(models.Model):
    tite = models.CharField(max_length=250)
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    data = models.DateField()
    text = models.TextField()

