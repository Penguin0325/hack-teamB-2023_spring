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
            return render(request, 'back/login.html', {})

    else:  # 初回アクセス時…空のフォームがほしいとき
        print('ミス')
        form = UserForm()

    return render(request, 'back/register.html', {"user_form": form})
    # return render(request, template_name)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)

    else:
        form = LoginForm()

    param = {
        'form': form,
    }

    return render(request, 'back/login.html', param)


# # class loginDeta():
#     # @csrf_protect
# class registerDetaView(TemplateView):
#     # template_name="back/register.html"
#     def __init__(self):
#         self.params = {
#         "UserCreate":False,
#         "user_form":UserForm(),
#         }

#     def get(self,request):
#         print("helo")
#         self.params["user_form"] = UserForm()
#         self.params["UserCreate"] = False

#         print('あああああああああああああああ')
#         print(request)
#         # self.params["account_form"] = UserForm(data=request.POST)

#         # # #フォーム入力の有効検証
#         # if self.params["user_form"].is_valid():
#         #     # アカウント情報をDB保存
#         #     account = self.params["user_form"].save()
#         #     account.save()
#         #     # アカウント作成情報更新
#         #     self.params["UserCreate"] = True
#         #     print('保存できたよ')

#         # else:
#         #     # フォームが有効でない場合
#         #     print(self.params["user_form"].errors)
#         #     # print(self.params["user_form"])
#         #     print('エラーです')
#         #     return redirect('back/register.html')

#         return render(request,"back/register.html",context=self.params)
#         # return render(request,"back/register.html")

#         # return HttpResponse('hello')
#     #Post処理
#     def post(self,request):
#         print('あああああああああああああああ')
#         print(request.POST["name"])
#         print(request)
#         # self.params["account_form"] = UserForm(data=request.POST)

#         # #フォーム入力の有効検証
#         if self.params["user_form"].is_valid().is_valid():
#             # アカウント情報をDB保存
#             account = self.params["user_form"].save()
#             account.save()

#             # アカウント作成情報更新
#             self.params["UserCreate"] = True

#         else:
#             # フォームが有効でない場合
#             print(self.params["user_form"].errors)

#         return render(request,"back/register.html",context=self.params)

    # if request.method == "POST":

    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         form = UserForm()
    #     param = {
    #         'form':form
    #     }
    # name = request.POST["name"]
    # loginID = request.POST["loginID"]
    # password = request.POST["password"]

    # d_today = datetime.date.today()
    # print(d_today)
    # user = User.objects.create_user('username', 'foo@example.com', 'password')

    # print("---------------------------------------")
    # obj=User(name='sika', loginID='sikasann', password='sikasann', createDate=d_today, last_login=d_today)
    # print(obj)
    # obj.save()
    # print("---------------------------------------")
    # id int, name varchar(20), loginID varchar(20) unique, password varchar(20), createDate date, updateDate date, deleteDate date
    # return render(request, template_name, param)


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

        # if user:
        #     if user.is_active:
        #         # ログイン
        #         login(request,user)
        #         # ホームページ遷移
        #         return HttpResponseRedirect(reverse('home'))
        #     else:
        #         # アカウント利用不可
        #         return HttpResponse("アカウントが有効ではありません")
        #         # ユーザー認証失敗
        # else:
        #         return HttpResponse("ログインIDまたはパスワードが間違っています")
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
