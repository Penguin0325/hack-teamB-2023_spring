from django.urls import path
from . import views
from django.conf.urls import url
from .views import loginDetaView, listDetaView, ImageUploadView, ImgDetaView, IconListView
from django.contrib import admin
from django.views import View
# from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path("", loginDetaView, name='login'),
    path("list/", listDetaView, name='list'),
    path("image-upload/images/", ImgDetaView, name='image'),
    path("image-upload/", ImageUploadView.as_view(), name="image-upload"),
    path("iconlist/", IconListView, name="iconlist")

    # path('auth/', obtain_jwt_token),
]
