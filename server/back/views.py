from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# from .models import UserModel, Account
from .forms import ImageUploadForm
import MySQLdb
import datetime

from django.views.generic import TemplateView # テンプレートタグ
from .forms import AccountForm, AddAccountForm # ユーザーアカウントフォーム


class  AccountRegistration(TemplateView):
    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    # Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"back/register.html",context=self.params)

    # Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        # フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"back/register.html",context=self.params)


# class loginDeta():
    # @csrf_protect
def signupDetaView(request):
    template_name="back/register.html"

    if request.method == "POST":

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
        userID = request.POST["userid"]
        password = request.POST["password"]

        user = authenticate(username=userID, password=password)
        print(user)

        print("---------------------------------------")

        if user:
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('home'))
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

#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('Login'))

#ホーム
@login_required
def home(request):
    params = {"UserID":request.user,}
    return render(request, "back/home.html",context=params)


#新規登録
class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    #Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"back/register.html",context=self.params)

    #Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        #フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"back/register.html",context=self.params)



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
