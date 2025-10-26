from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def profile(request):
    # user_data = {
    #     "name" : "Rahim",
    #     "age" : 10
    # }
    marks = [
        {
            "id" : 1,
            "subject" : "Math",
            "marks" : 80
        },
        {
            "id" : 2,
            "subject" : "Englist",
            "marks" : 40
        },
        {
            "id" : 3,
            "subject" : "Bangla",
            "marks" : 70
        },
        {
            "id" : 4,
            "subject" : "Commerce",
            "marks" : 90
        },
      ]
    data = "2023-01-12T10:30:00.000123"
    date = datetime.fromisoformat(data)
    print(date)
    return render(request,'student/index.html', {"marks" : marks, "age" : 20, "Name": "Arman Islam","1st" : ["apple","orange","banana"],"dates": date})

def home(request):
    return HttpResponse("I am a home")
