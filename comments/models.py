from django.db import models

# Create your models here.


class Single(models.Model):
    title = models.ForeignKey('', on_delete=models.CASCADE, related_name='single')
    body = models.TextField()
    users = [
        'id',
        'photo',
    ]

    def __str__(self):
        return (self.title, self.body, self.users)