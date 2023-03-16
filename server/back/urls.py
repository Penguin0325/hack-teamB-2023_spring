from django.urls import path
from . import views
from django.conf.urls import url
from .views import loginDetaView, listDetaView, ImageUploadView, ImgDetaView, IconListView,registerDetaView
from django.contrib import admin
from django.views import View
# from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path("login/",loginDataView, name='login'),
    path("register/",registerDetaView, name='register'),
    path("list/",listDetaView, name='list'),
    path("image-upload/image/",ImgDetaView,name='image'),
    path("image-upload/", ImageUploadView.as_view(), name="image-upload"),
    path("iconlist/", IconListView, name="iconlist")
    path("home",views.home,name="home"),
    
    # path('auth/', obtain_jwt_token),
]
