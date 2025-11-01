from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog

def home(request):
    return render(request,'index.html')

a = 12
b = {'name':'Arman','age':24}
def hello(request):
    return render(request, 'hello.html',context={'a':a,'b':b})

def about(request):
    #fetch all data
    #select * from Blog
    blogs = Blog.objects.all()
    return render(request, 'about.html',{'blogs':blogs})
