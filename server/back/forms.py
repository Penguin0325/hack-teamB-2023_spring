from django import forms
from django.db import models
from .models import ImageUpload, User, UserManager
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import AbstractBaseUser


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = "__all__"


class PhotoForm(forms.Form):
    image = forms.ImageField()


class LoginForm(AuthenticationForm):
    pass


class UserForm(forms.ModelForm):
    class Meta():
        model = User
        print(model)
        # fields = "__all__"
        fields = {'name', 'loginID', 'password'}
        labels = {'username': "ユーザーネーム",
                  'loginID': "ログインID", 'password': "パスワード"}

# フォームクラス作成
# class AccountForm(forms.ModelForm):
#     # パスワード入力：非表示対応
#     password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

#     class Meta():
#         # ユーザー認証
#         model = User
#         # フィールド指定
#         fields = ('username','email','password')
#         # フィールド名指定
#         labels = {'username':"ユーザーID",'email':"メール"}

# class AddAccountForm(forms.ModelForm):
#     class Meta():
#         # モデルクラスを指定
#         model = Account
#         fields = ('id','last_name','first_name',)
#         labels = {'id':'id','last_name':"苗字",'first_name':"名前",}

#         # fields = ('id','createDate')
#         # labels = {'id':"id",'createDate':"作成日"}

# fields = ('last_name','first_name','account_image',)
# labels = {'last_name':"苗字",'first_name':"名前",'account_image':"写真アップロード",}
