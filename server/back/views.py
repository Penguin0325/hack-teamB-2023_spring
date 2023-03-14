from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import CreateView
from .models import TestModel, UserModel,ImageUpload
from .forms import ImageUploadForm
import MySQLdb
import datetime


# class loginDeta():
    # @csrf_protect
def loginDetaView(request):
    template_name="back/test.html"
    #     if request.headers.get("Content-Type") == "loginDeta/json":
    #         tasks = Task.object.values()
    #         tasks_list = list(tasks)
    #         return JsonResponse(tasks_list, safe=False, status=200)


    if request.POST:
        name = request.POST["name"]
        loginID = request.POST["loginID"]
        password = request.POST["password"]
        
        d_today = datetime.date.today()
        print(d_today)

        obj=UserModel(name=name, loginID=loginID, password=password, createDate=d_today, deleteDate=d_today)
        obj.save()
    # id int, name varchar(20), loginID varchar(20) unique, password varchar(20), createDate date, updateDate date, deleteDate date

    return render(request, template_name)


def listDetaView(request):
    template_name="back/list.html"
    ctx = {}
    sample_users = UserModel.objects.values('id', 'name')
    print(sample_users)
    ctx["object_list"] = sample_users
    return render(request, template_name, ctx)

# @csrf_protect
class ImageUploadView(CreateView):
    template_name = "back/image-upload.html"
    form_class = ImageUploadForm
    success_url = "image/"


def ImgDetaView(request):
    template_name="back/image.html"
    # ctx = {}
    # img_path = ImageUpload.objects.values('img')
    # print(img_path)
    # ctx["object_list"] = img_path
    return render(request, template_name)

def IconListView(request):
    template_name='back/iconlist.html'
    ctx = {}
    img_path = ImageUpload.objects.values('img')
    print(img_path)
    ctx["object_list"] = img_path
    return render(request, template_name)
