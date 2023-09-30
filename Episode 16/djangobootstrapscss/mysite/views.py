from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Portopolio',
    }
    return render(request, 'index.html', context)

def login(request):
    context = {
        'title':'Login',
    }
    return render(request, 'login.html', context)

def daftar(request):
    context = {
        'title':'Daftar',
    }
    return render(request, 'daftar.html', context)