from django.http import HttpResponse

def home(request):
    print("hello")
    return HttpResponse("<h1>Arman</h1>")