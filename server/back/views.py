from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import TestModel
import MySQLdb


@csrf_protect
def loginDetaView(request):
    template_name="back/test.html"

    if request.POST:
        title = request.POST["title"]
        content = request.POST["content"]
        print(title)
        print(content)

        # obj=TestModel(id=1, name='pengin')
        # obj.save()
    
    return render(request, template_name)
