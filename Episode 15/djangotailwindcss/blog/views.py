from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'blog',
        'subtitle':'aku adalah halaman blog',
    }
    return render(request, 'index.html', context)