from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import CreateView
from .models import TestModel, UserModel
from .forms import ImageUploadForm
import MySQLdb
import datetime



@csrf_protect
def loginDetaView(request):
    template_name="back/test.html"

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
    success_url = "list/"

# def index(request):
#     template_name = 'back/root.html'
#     return render(request, template_name)


# def index(request):
#     context = {
#         'photos': Photo.objects.all(),
#     }

# @csrf_protect
# def photouploadDetaView(request):
#     if request.method == 'GET':
#         return render(request, 'back/photoupload.html', {
#         'form': PhotoForm(),
#     })

#     elif request.method == 'POST':
#         form = PhotoForm(request.POST, request.FILES)
#         if not form.is_valid():
#             raise ValueError('invalid form')

#         photo = Photo()
#         photo.image = form.cleaned_data['image']
#         print(photo.image)
#         photo.save()
    
#         return redirect('/')
#     # return render(request, '')