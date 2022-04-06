from django.contrib import admin

from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('like-api/', include('like.urls')),
    path('api/users/', include('users.urls')),
    path('single/api', include('comments.urls'))
]

