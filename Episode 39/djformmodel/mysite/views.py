from django.shortcuts import render


def index(request):
    context = {
        'Judul': 'Beranda',
        'Heading': 'Selamat datang.',
    }
    return render(request, 'index.html', context)
