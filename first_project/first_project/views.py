from django.http import HttpResponse

def home(request):
    return HttpResponse ("This is first django page")

def about(request):
    return HttpResponse ("This is about page")