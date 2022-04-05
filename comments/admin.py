from django.contrib import admin
from comments.models import Single, Rating

# Register your models here.
admin.site.register(Rating)
admin.site.register(Single)