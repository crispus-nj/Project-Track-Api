from django.contrib import admin

from comments.models import Rating
from .models import Project

# Register your models here.
admin.site.register(Project)
admin.site.register(Rating)