from django.db import models
from accounts.models import Account
from projects.models import Project

# Create your models here.
like_choices = (
    ('like', 'like'),
    ('unlike', 'unlike')
)

class Like(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True ,related_name="users")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True ,related_name="projects")
    choices = models.CharField(choices=like_choices, max_length=10)
