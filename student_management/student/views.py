from django.shortcuts import render,HttpResponse,redirect
from . import models
from . import forms
from django.contrib import messages
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
def create_student(request):
   
    if request.method == "POST":
        form = forms.StudentForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           messages.add_message(request, messages.SUCCESS, 'Student updated successfully.')
           return redirect('home')
    else:
         form = forms.StudentForm()
    return render(request,'student/create_edit_student.html',{'form':form})
    
def home(request):
    students = models.Student.objects.all()
    return render(request,'student/index.html',{'students':students})

def updated_student(request,id):
    student = models.Student.objects.get(id=id)
    form = forms.StudentForm(instance=student)
    # form = forms.StudentForm()
    if request.method == "POST":
        form = forms.StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student updated successfully.')
            return redirect('home')
    return render(request,'student/create_edit_student.html',{'form':form, 'edit':True})

def delete_student(request,id):
    student = models.Student.objects.get(id=id)
    messages.add_message(request, messages.SUCCESS, 'Student delete successfully.')
    student.delete()
    return redirect('home')