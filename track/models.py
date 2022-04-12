from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Track(models.Model):
    image = CloudinaryField("image")
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name