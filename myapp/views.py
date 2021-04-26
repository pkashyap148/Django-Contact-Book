from django.shortcuts import render
from .models import directory
# Create your views here.
def home(req):
    flag = False
    if req.method == 'POST':
        new_name = req.POST.get('name').title()
        new_phone = req.POST.get('number')
        directory.objects.create(name=new_name, number=new_phone)
        flag = True
        print(new_name+" "+new_phone+" added successfully")
    context = {
        'f' : flag
        }   
    return render(req,'index.html', context)

def phonebook(req):
    det=''
    x = 0
    obj = directory.objects.all()
    # search
    if req.method == 'POST':
        search = req.POST.get('searchname').title()
        for i in obj:
            if search in i.name:
                x = 1
                det = i.number
            else:
                x = 2
    print(x)
    context = {
        'obj': obj,
        'x' : x,
        'det': det
    }
    return render(req, 'directory.html',context)

def deletecont(req):
    flag = False
    if req.method == 'POST':
        del_name = req.POST.get('delname').title()
        obj = directory.objects.get(name = del_name)
        obj.delete()
        print(del_name+" is deleted")
        flag = True
    context = {
        'f' : flag
        }  
    return render(req, 'delete.html', context)

