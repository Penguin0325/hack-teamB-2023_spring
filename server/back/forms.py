from django import forms
from .models import ImageUpload
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = "__all__"

class PhotoForm(forms.Form):
    image = forms.ImageField()

class LoginForm(AuthenticationForm):
    pass