from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
# from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import ImageUpload, User, UserPostList
from .forms import ImageUploadForm, UserForm, LoginForm
import MySQLdb
import datetime
from django.contrib.auth import login

from django.views.generic import TemplateView  # テンプレートタグ
# from .forms import AccountForm, AddAccountForm # ユーザーアカウントフォーム

# class loginDeta():
# @csrf_protect

# class  AccountRegistration(TemplateView):
#     def __init__(self):
#         self.params = {
#         "AccountCreate":False,
#         "account_form": AccountForm(),
#         "add_account_form":AddAccountForm(),
#         }

#     # Get処理
#     def get(self,request):
#         self.params["account_form"] = AccountForm()
#         self.params["add_account_form"] = AddAccountForm()
#         self.params["AccountCreate"] = False
#         return render(request,"back/register.html",context=self.params)

#     # Post処理
#     def post(self,request):
#         self.params["account_form"] = AccountForm(data=request.POST)
#         self.params["add_account_form"] = AddAccountForm(data=request.POST)

#         # フォーム入力の有効検証
#         if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
#             # アカウント情報をDB保存
#             account = self.params["account_form"].save()
#             # パスワードをハッシュ化
#             account.set_password(account.password)
#             # ハッシュ化パスワード更新
#             account.save()

#             # 下記追加情報
#             # 下記操作のため、コミットなし
#             add_account = self.params["add_account_form"].save(commit=False)
#             # AccountForm & AddAccountForm 1vs1 紐付け
#             add_account.user = account

#             # モデル保存
#             add_account.save()

#             # アカウント作成情報更新
#             self.params["AccountCreate"] = True

#         else:
#             # フォームが有効でない場合
#             print(self.params["account_form"].errors)

#         return render(request,"back/register.html",context=self.params)


def registerDetaView(request):
    template_name = "back/register.html"
    if request.method == "POST":  # フォームの入力を終えてすべてのフォームのデータともにviewに戻るとき
        form = UserForm(request.POST)  # ProfileFormを作る（？）

        if form.is_valid():  # フォームの値が正しい時
            print('成功')
            question = form.save(commit=False)  # フォームを保存 ※commit=Falseでまだ保存しない
            question.user = request.user
            question.save()

            return render(request, 'back/home.html', {})
    
    else: #初回アクセス時…空のフォームがほしいとき

        form = UserForm()

    return render(request, 'back/register.html', {"user_form": form})

def login_view(request):
    print('request.method == POST')
    print(request.method)
    # ↑GET
    if request.method == 'POST':
        # print(LoginForm(request, data=request.POST))
        form = LoginForm(request, data=request.POST)
        print(form)
        # form = LoginForm(request, data=request.POST)
        print(form)
        if form.is_valid():
            print('成功')
            user = form.get_user()
            if user:
                login(request, user)
            return render(request, 'back/home.html', {})
        else:
            print('そんな値はないです')
            for ele in form :
                print(ele)
    else:

        form = LoginForm()

    return render(request, 'back/login.html', {'form': form})



# ログインフォームから送信されてきたユーザーの情報で認証
# 認証 OK の場合にそのユーザーの状態をログイン状態に設定する
def loginDataView(request):
    template_name = 'back/login.html'
    if request.method == "POST":
        loginID = request.POST["loginID"]
        password = request.POST["password"]
        print(loginID)
        print(password)

        user = authenticate(loginID=loginID, password=password)
        print(user)
        use_loginId = User.objects.get(loginID=loginID)
        use_password = User.objects.filter(password=password)
        print(use_password)
        print(use_loginId)

        print("---------------------------------------")

        if use_password.first() is None:
            return HttpResponse("パスワードが違います")
        else:
            for p in use_password:
                if p.id == use_loginId.id:
                    # user.is_active = True;
                    print('ログインできます')
                    request.user.is_authenticated == True
                    login(request, p.loginID)
                    return HttpResponseRedirect(reverse('home'))

        print("---------------------------------------")

        
    return render(request, template_name)

   

# ログアウト


@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('Login'))

# ホーム


@login_required
def home(request):
    params = {"UserID": request.user, }
    return render(request, "back/home.html", context=params)


def listDetaView(request):
    template_name = "back/list.html"
    ctx = {}
    sample_users = User.objects.values('id', 'name')
    print(sample_users)
    ctx["object_list"] = sample_users

    return render(request, template_name, ctx)


# @csrf_protect


class ImageUploadView(CreateView):
    template_name = "back/image-upload.html"
    form_class = ImageUploadForm
    success_url = "images/"


def ImgDetaView(request):
    template_name = "back/image.html"
    # ctx = {}
    # img_path = ImageUpload.objects.values('img')
    # print(img_path)
    # ctx["object_list"] = img_path
    return render(request, template_name)


def IconListView(request):
    template_name = 'back/iconlist.html'
    ctx = {}
    img_path = ImageUpload.objects.values('title', 'img')
    print(img_path)
    ctx["object_list"] = img_path
    return render(request, template_name, ctx)


class UserStatusView(View):
    def get(self, request, *args, **kwargs):
        user_inf = UserPostList.objects.all

        return render(request, 'back/user-list.html', {
            'user_inf': user_inf,
        })
