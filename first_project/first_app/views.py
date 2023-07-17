from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse ("This is first django page")

def about(request):
    return HttpResponse ("This is about page")
