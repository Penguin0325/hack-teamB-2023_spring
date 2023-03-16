from django.urls import path
from . import views
from django.conf.urls import url
from .views import loginDataView, listDetaView, ImageUploadView, ImgDetaView, IconListView,registerDetaView, login_view,logout_view
from django.contrib import admin
from django.views import View
# from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # path('signup/', views.signup_view, name='signup'),
    path("login/", login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path("register/",registerDetaView, name='register'),
    path("list/",listDetaView, name='list'),
    path("image-upload/image/",ImgDetaView,name='image'),
    path("image-upload/", ImageUploadView.as_view(), name="image-upload"),
    path("iconlist/", IconListView, name="iconlist"),
    path("home/",views.home,name="home"),
    
    # path('auth/', obtain_jwt_token),
]
