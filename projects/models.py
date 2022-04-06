from django.db import models
from cloudinary.models import CloudinaryField
from accounts.models import Account
from track.models import Track

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    image= CloudinaryField('image')
    description = models.CharField(max_length=30)
    technologies = models.CharField(max_length=500)
    github_link = models.URLField()
    track = models.ForeignKey(Track, on_delete=models.SET_NULL, null=True)
    liked = models.ManyToManyField(Account, null=True, blank=True, related_name='liked')
    date_created = models.DateField(auto_now_add=True)
    date_updated= models.DateField(auto_now=True)

    @property
    def num_likes(self):
        return self.liked.all().count()

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects
    
    def save_project(self):
        self.save()   

    def __str__(self):
        return str(self.name)