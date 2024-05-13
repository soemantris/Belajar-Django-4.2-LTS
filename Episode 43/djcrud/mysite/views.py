from django.shortcuts import render


def index(request):
    context = {
        'Judul': 'Beranda',
        'Heading': 'Selamat datang di aplikasi pulang dan pergi',
    }
    return render(request, 'index.html', context)
