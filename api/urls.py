from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.api_routes, name="routes"),
    path('projects/', include('projects.urls')),
    path('like-api/', include('like.urls')),
    path('users/', include('users.urls')),
    path('single-project/', include('comments.urls'))
]
