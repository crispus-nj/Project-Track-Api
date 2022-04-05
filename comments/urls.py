from django.urls import path
from . import views


urlpatterns = [
    path('', views.singleDetailOverview, name = 'single_detail_overview'),
    path('', views.ratingDetailOverview, name = 'rating_detail_overview'),
]
   