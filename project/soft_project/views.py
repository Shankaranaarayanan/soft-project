from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def home_page(request):
    if request.method=='POST':
        path = request.POST.get('text')
        text = request.POST.get('content')
        l=find_files(path,text)
        return render(request,'soft_project/test.html',{'list':l})
    return render(request,template_name='soft_project/test.html')


def find_files(path,key):
    l=[]
    for i in os.listdir(path):
        if key.lower() in i.lower():
            l.append(i)
        filepath=path+'/'+i
        if(os.path.isfile(filepath)):
            file = open(filepath)
            for j in file:
                if key in j:
                    l.append(i)
            file.close()
        else:
            for i in find_files(filepath,key):
                l.append(i)
    return l