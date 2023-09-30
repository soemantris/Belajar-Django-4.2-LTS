from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Kontak',
    }
    return render(request, 'kontak/index.html', context)