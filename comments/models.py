from django.db import models
from accounts.models import Account
from projects.models import Project

# Create your models here.

class Single(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    users = models.ManyToManyField(Account, on_delete=models.SET_NULL, null=True, related_name='members')

    def __str__(self):
        return self.Project



class Rating(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE),
    user = models.ForeignKey(Account, on_delete=models.CASCADE),
    rating = models.FloatField()


    def __str__(self):
        return self.rating


