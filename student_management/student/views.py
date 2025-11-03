from django.shortcuts import render,HttpResponse
from . import models
from . import forms
# Create your views here.
# def home(request):
#     print(request.POST)
#     if request.method == "POST":
#         name = request.POST.get("name")
#         inputEmail = request.POST.get("inputEmail")
#         inputPhone = request.POST.get("inputPhone")
#         inputPassword = request.POST.get("inputPassword")
#         checkbox = request.POST.get("checkbox")
#         photo = request.FILES.get("photo")
#         print(request.FILES)
#         if checkbox == "on":
#             checkbox = True
#         else:
#             checkbox = False

#         student = models.Student(name=name, inputEmail=inputEmail, inputPhone=inputPhone, inputPassword=inputPassword, checkbox=checkbox, photo=photo)
#          #sutdent class object
#         student.save()
#         return HttpResponse("Data saved successfully")
#     return render(request,'student/index.html')


#This is the Model form
def home(request):
   
    if request.method == "POST":
        form = forms.StudentForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           return HttpResponse("student object created successfully")
    else:
         form = forms.StudentForm()
    return render(request,'student/index.html',{'form':form})
    
def student_list(request):
    students = models.Student.objects.all()
    return render(request,'student/index.html',{'students':students})
