from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import UserModel
from .forms import ImageUploadForm
import MySQLdb
import datetime


# class loginDeta():
    # @csrf_protect
def signupDetaView(request):
    template_name="back/test.html"
    #     if request.headers.get("Content-Type") == "loginDeta/json":
    #         tasks = Task.object.values()
    #         tasks_list = list(tasks)
    #         return JsonResponse(tasks_list, safe=False, status=200)


    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        # if form.is_valid():
        #     new_user = form.save()
        #     print(new_user)



        name = request.POST["name"]
        loginID = request.POST["loginID"]
        password = request.POST["password"]
        
        d_today = datetime.date.today()
        print(d_today)

        # user = User.objects.create_user('username', 'foo@example.com', 'password')

        # obj=UserModel(name=name, loginID=loginID, password=password, createDate=d_today, deleteDate=d_today)
        # obj.save()
    # id int, name varchar(20), loginID varchar(20) unique, password varchar(20), createDate date, updateDate date, deleteDate date

    return render(request, template_name)


# ログインフォームから送信されてきたユーザーの情報で認証
# 認証 OK の場合にそのユーザーの状態をログイン状態に設定する
def loginDataView(request):
    template_name='back/login.html'
    if request.method == "POST":
        loginID = request.POST["loginID"]
        password = request.POST["password"]

        user = authenticate(loginID=loginID, password=password)
        print(user)

        print("---------------------------------------")

        if user:
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('image-upload'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
                # ユーザー認証失敗
        else:
                return HttpResponse("ログインIDまたはパスワードが間違っています")
        # GET
    return render(request, template_name)

        # use_loginId = UserModel.objects.get(loginID=loginID)
        # use_password = UserModel.objects.filter(password=password)
        # print(use_password)

        # if use_password.first() is None:
        #     print("パスワードが違います")
        # else:
        #     for p in use_password:
        #         if p.id == use_loginId.id:
        #             print('ログインできます')
        #             request.user.is_authenticated == True
        #             login(request, p.name)
        #             return redirect("app:index")
        

        
    
    # return render(request, template_name)

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
    success_url = "list/"
