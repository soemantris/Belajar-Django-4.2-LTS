from django.shortcuts import render

def index(request):
    context = {
        'title':'portopolio',
        'subtitle':'Jika saya mencoba yang terbaik dan gagal, setidaknya saya telah melakukan yang terbaik.',
        'name':'jhon smith',
        'jobs':'Web Developers',
    }
    return render(request, 'index.html', context)