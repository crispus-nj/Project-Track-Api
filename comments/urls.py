from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('comments', views.SingleView)
router.register("rating", views.RatingView)



urlpatterns = [
    path('', include(router.urls))
]