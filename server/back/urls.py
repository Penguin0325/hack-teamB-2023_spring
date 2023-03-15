from django.urls import path
# from . import views
from django.conf.urls import url
from .views import listDetaView, ImageUploadView,loginDataView,signupDetaView
from django.contrib import admin
from django.views import View


urlpatterns = [
    path("signup/",signupDetaView, name='signup'),
    path("login/",loginDataView, name='login'),
    path("image-upload/list/",listDetaView, name='list'),
    path("image-upload/", ImageUploadView.as_view(), name="image-upload"),
]