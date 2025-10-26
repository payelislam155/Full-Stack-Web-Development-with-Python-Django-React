from django.shortcuts import render

def profile(request):
    return render(request,'teacher/index.html')

    return HttpResponse("I am a home")
