from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
# from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import ImageUpload, User, UserPostList, RoomModels, MessageModels, ImageConnectModels
from .forms import ImageUploadForm, UserForm, LoginForm,RoomForm,MessageForm, ImageChoiseForm
import MySQLdb
import datetime
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist

from django.views.generic import TemplateView  # テンプレートタグ

def rootView(request):
    return render(request, 'back/root.html')

def logout_view(request):
    return render(request, 'back/logout.html')


def registerDetaView(request):
    template_name = "back/register.html"
    if request.method == "POST":  # フォームの入力を終えてすべてのフォームのデータともにviewに戻るとき
        form = UserForm(request.POST)  # ProfileFormを作る（？）

        if form.is_valid():  # フォームの値が正しい時
            print('成功')
            question = form.save(commit=False)  # フォームを保存 ※commit=Falseでまだ保存しない
            # question.user = request.user
            # question = User(loginID = form.changed_data["loginID"])
            question.set_password(form.cleaned_data["password"])
            question.save()

            return render(request, 'back/login.html', {})
    
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
    return HttpResponseRedirect(reverse('back:Login'))

# ホーム
@login_required
def home(request):
    params = {"name": request.user, }
    return render(request, "back/home.html", context=params)

@login_required
def roomView(request):
    template_name = "back/room.html"
    form = RoomForm(data=request.POST)
    print(form)
    # if request.POST:
    if form.is_valid():
        #DBに登録する準備を行う
        thread = form.save(commit=False)
        #threadにログイン中ユーザー情報を追加
        thread.user = request.user
        #DBに登録
        thread.save()
        return HttpResponseRedirect(reverse('back:roomlist'))

    return render(request, template_name, {"form": form})

@login_required
def roomListView(request):
    template_name = "back/roomlist.html"
    form = RoomForm()
    print(form)
    ctx = {}
    qs = RoomModels.objects.values('id','roomname')
    ctx["object_list"] = qs
    return render(request, template_name, ctx)

def messageView(request, thread_id):
    template_name = "back/message.html"

    threads = RoomModels.objects.filter(pk=thread_id).values()
    thread  = threads[0]
    username_dicts = User.objects.filter(pk=threads[0]['user_id']).values('name')
    thread.update(username_dicts[0])
    #該当する掲示板に紐づくコメントを取得
    comments = MessageModels.objects.filter(room_id=thread_id).values()
    count = len(comments)
    #コメントのユーザーIDからユーザー名を取得してオブジェクトに追加
    for count in range(count):
        username_dicts = User.objects.filter(pk=comments[count]['user_id']).values('name')
        comments[count].update(username_dicts[0])
    #フォーム作成
    form = MessageForm
    context = {
        'thread': thread,
        'comments': comments,
        'form': form,
    }
    return render(request, template_name, context)

def messageAddView(request):
    template_name = 'back:message'
    
    thread_id_tmp = request.POST['thread_id']
    print("------form----------------")
    test = thread_id_tmp.isdecimal()
    print(test)
    thread_id = int(thread_id_tmp)
    print(type(thread_id))
    form = MessageForm(data=request.POST)
    print(form)
    print("-----is_valid-----------------")
    print(form.is_valid())
    
    if form.is_valid():
        comment = form.save(commit=False)
        # #threadにログイン中ユーザー情報e
        comment.user = request.user
        print(comment.user)
        # int(thread_id)
        comment.room_id = thread_id
        print("----------------------")
        print(comment.room_id)
        print(type(comment.room_id))
        print(comment.room)
        print(comment.contest)
        print(comment.create_date)
        print("----------------------")
        #DBに登録
        comment.save()
        print('comment.save()')
    return redirect(template_name, thread_id=thread_id)
    
    # return render(request, template_name)


def listDetaView(request):
    template_name = "back/list.html"
    sample_users = User.objects.values('id', 'name')
    img_list = ImageUpload.objects.values('id','title','img')
    connect = ImageConnectModels.objects.values('id', 'user', 'icon')
    context = {
        'users': sample_users,
        'images': img_list,
        'connect': connect
    }
    print(sample_users)
    return render(request, template_name, context)
# @csrf_protect


class ImageUploadView(CreateView):
    template_name = "back/image-upload.html"
    form_class = ImageUploadForm
    success_url = "image/"


def ImgDetaView(request):
    # template_name = "image-upload/image"
    # ctx = {}
    # img_path = ImageUpload.objects.values('img')
    # print(img_path)
    # ctx["object_list"] = img_path
    return render(request, 'back/image.html')


def IconListView(request):
    template_name = 'back/iconlist.html'
    ctx = {}
    img_path = ImageUpload.objects.values('id','title','img')
    
    person_count = ImageUpload.objects.count()
    # print(ImageUpload.objects.get(id=1))
    print('aaaaaaaaaaaa')
    # print(img_path.values('title'))
    ctx["object_list"] = img_path
    user_id = request.user.id
    range(person_count)
    # for val in range(person_count):
    print(request.method)
    if request.method == 'POST':
        for i in img_path:
            get_button = i.get('title')
            save_id = i.get('id')
            if get_button in request.POST:
                print(get_button)
                try:
                    img_ing = ImageConnectModels.objects.get(user=user_id, icon=save_id, is_published=1)
                    print("保存済み")
                    # redirect_url = "/back/login"
                    # return HttpResponseRedirect(redirect_url)
                    # return redirect('list')
                    ImageConnectModels.objects.filter(user=user_id, icon=save_id, is_published=1).delete()
                except ObjectDoesNotExist:
                    print("ないよ")
                    image = ImageConnectModels(user=user_id, icon=save_id, is_published=1)
                    image.save()


            # get_button = i.get('title')
            # save_id = i.get('id')
            # if get_button in request.POST:
            #     print('OK')
            #     if not ImageConnectModels.objects.get(user=user_id, icon=save_id, is_published=1):
            #         print('ないよ')
            #     elif ImageConnectModels.objects.get(user=user_id, icon=save_id, is_published=1):
            #         print('保存済み')
            #         # image = ImageConnectModels(user=user_id, icon=save_id, is_published=1)
            #         # image.save()

        # ---------チェックボックス---------
        # # print(request.POST.get('パチンコ'))
        # my_checkbox_value = request.POST.getlist("option")
        # checkbox_num = len(my_checkbox_value)
        # # num個目のチェックボックスの処理
        # for num in range(checkbox_num):
        #     if my_checkbox_value:
        #         print('取れたよ')
        #         image = ImageConnectModels(user=user_id, icon=my_checkbox_value[num], is_published=0)
        #         image.save()
        #     else:
        #         print(my_checkbox_value)
        #         print('取れなかったよ')
        # ---------チェックボックス---------

    return render(request, template_name, ctx)

def IconDeleteView(request):
    template_name = 'back/icondelete.html'
    sample_users = User.objects.values('id', 'name')
    img_list = ImageUpload.objects.values('id','title','img')
    connect = ImageConnectModels.objects.values('id', 'user', 'icon')
    user_id = request.user.id
    count = ImageConnectModels.objects.count()
    for val in range(count):
        # print(val+1)
        imgIng= ImageConnectModels.objects.values('user').get(id=val+1)
        values_user = imgIng['user']
        if user_id==values_user:
            img = ImageConnectModels.objects.get(id=val)
            print(type(img))
            


    return render(request, template_name)


class UserStatusView(View):
    def get(self, request, *args, **kwargs):
        user_inf = UserPostList.objects.all

        return render(request, 'back/user-list.html', {
            'user_inf': user_inf,
        })
