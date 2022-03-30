from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Project(models.Model):
    image = CloudinaryField('image')
    description = models.CharField(max_length=30)
    technologies = models.CharField(max_length=500)
    github_link = models.URLField()
    date_created = models.DateField(auto_now_add=True)
    date_updated= models.DateField(auto_now_add=True)
    liked = models.ManyToManyField(null=True, blank=True, related_name='liked')

    @property
    def num_likes(self):
        return self.liked.all().count()

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects
    
    def save_project(self):
        self.save()   
