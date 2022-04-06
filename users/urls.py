from xml.etree.ElementInclude import include
from django.urls import path, include
from rest_framework import routers

from users import views
router = routers.DefaultRouter()
router.register("create", views.CreateUserView)

app_name = 'users'


urlpatterns = [
    path('create/', include(router.urls), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]

