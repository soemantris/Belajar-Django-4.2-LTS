from django.shortcuts import render


def index(request):
    context = {
        'Judul': 'Home',
        'Heading': 'Selamat datang di halaman home',
    }
    return render(request, 'index.html', context)
