from xml.etree.ElementInclude import include
from django.urls import path
# from rest_framework import routers

from users import views

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('user/', views.ManageUserView.as_view(), name='user'),
]

