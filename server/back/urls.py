from django.urls import path
from . import views
from django.conf.urls import url
from .views import listDetaView, ImageUploadView,loginDataView,signupDetaView,AccountRegistration
from django.contrib import admin
from django.views import View


urlpatterns = [
    path("register/",views.AccountRegistration.as_view(), name='register'),
    path("login/",loginDataView, name='login'),
    path("image-upload/list/",listDetaView, name='list'),
    path("image-upload/", ImageUploadView.as_view(), name="image-upload"),
    path("home",views.home,name="home"),
]