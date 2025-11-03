from django.shortcuts import render
from . import models
from django.http import HttpResponse

# Create your views here.
def home(request):
    print(request.POST)
    if request.method == "POST":
        name = request.POST.get("name")
        inputEmail = request.POST.get("inputEmail")
        inputPhone = request.POST.get("inputPhone")
        inputPassword = request.POST.get("inputPassword")
        checkbox = request.POST.get("checkbox")
        photo = request.FILES.get("photo")
        print(request.FILES)
        if checkbox == "on":
            checkbox = True
        else:
            checkbox = False

        student = models.Student(name=name, inputEmail=inputEmail, inputPhone=inputPhone, inputPassword=inputPassword, checkbox=checkbox, photo=photo)
         #sutdent class object
        student.save()
        return HttpResponse("Data saved successfully")
    return render(request,'student/index.html')
    
