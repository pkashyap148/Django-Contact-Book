from django.shortcuts import render
from .models import directory
# Create your views here.
def home(req):
    flag = False
    if req.method == 'POST':
        new_name = req.POST.get('name')
        new_phone = req.POST.get('number')
        directory.objects.create(name=new_name, number=new_phone)
        flag = True
        print(new_name+" "+new_phone+" added successfully")
    context = {
        'f' : flag
        }   
    return render(req,'index.html', context)

def phonebook(req):
    obj = directory.objects.all()
    context = {
        'obj': obj
    }
    return render(req, 'directory.html',context)