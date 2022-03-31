from django.urls import path
from . import views


urlpatterns = [
    path('', views.commentOverview, name = 'comment-overview'),
]