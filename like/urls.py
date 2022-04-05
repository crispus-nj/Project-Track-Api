from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('like_unlike', views.LikeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
