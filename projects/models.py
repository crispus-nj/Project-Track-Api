from django.db import models


# Create your models here.
class Project(models.Model):
    image= models.ImageField()
    description = models.CharField(max_length=30)
    technologies = models.CharField(max_length=500)
    github_link = models.URLField()
    date_created = models.DateField(auto_now_add=True)
    date_updated= models.DateField(auto_now_add=True)

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects
    
    def save_project(self):
        self.save()   
