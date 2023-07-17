from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, './first_app/index.html', {'author': 'Phitron', 'age': 19, 'marks': 88, 'namme':"this is"})