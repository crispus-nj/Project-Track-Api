from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register("getProjects", views.Projects)
router.register('projects', views.ProjectView)

urlpatterns = [
   path('', include(router.urls) ),
   path('getProjects', views.Projects.as_view(), name="getProject")
]