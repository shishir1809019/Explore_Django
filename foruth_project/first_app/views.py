from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, './first_app/home.html', {"name": "I am Rhahim", "marks": 86,
        "courses": [
            {
                "id": 1,
                "course": "C",
                "teacher": "Rahim"
            },
            {
                "id": 2,
                "course": "C++",
                "teacher": "Fahim"
            },
            {
                "id": 1,
                "course": "C",
                "teacher": "Halim"
            }
        ]})
    
def about(request):
    return render(request, './first_app/about.html',{'author': 'mr. max'})