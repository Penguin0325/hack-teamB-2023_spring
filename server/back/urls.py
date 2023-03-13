from django.urls import path
from.views import loginDetaView
 
urlpatterns = [
    path("",loginDetaView),
]