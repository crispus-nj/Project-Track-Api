from atexit import register
from django.contrib import admin
from comments.models import Single, Rating

# Register your models here.
admin.site.register(Single)
admin.site.register(Rating)