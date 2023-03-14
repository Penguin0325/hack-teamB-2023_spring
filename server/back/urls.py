from django.urls import path
from . import views
from django.conf.urls import url
from .views import loginDetaView, listDetaView, ImageUploadView
from django.contrib import admin
from django.views import View
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path("",loginDetaView, name='login'),
    path("image-upload/list/",listDetaView, name='list'),
    path("image-upload/", ImageUploadView.as_view(), name="image-upload"),
    path('auth/', obtain_jwt_token),
]