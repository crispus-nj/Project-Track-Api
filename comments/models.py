from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Single(models.Model):
    name = models.ForeignKey('title', on_delete=models.CASCADE, related_name='name')
    body = models.TextField()
    users = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return (self.body)




class Rating(models.Model):
    project = models.ForeignKey('project', on_delete=models.CASCADE, related_name='project')
    user = models.ForeignKey(User, default=1)
    rating = models.FloatFiled()

    def __str__(self):
        return (self.rating)




