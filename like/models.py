from django.db import models
from django.contrib.auth.models import User
# Create your models here.
like_choices = (
    ('like', 'like'),
    ('unlike', 'unlike')
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    # post = ''
    choices = models.CharField(choices=like_choices, max_length=10)
