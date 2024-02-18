from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'Judul': 'Blog',
        'Heading': 'Halaman Blog',
    }
    return render(request, 'blog/index.html', context)


def daftar_artikel(request):
    context = {
        'Judul': 'Daftar Artikel',
        'Heading': 'Halaman Daftar Artikel',
    }
    return render(request, 'blog/index.html', context)


def detail_artikel(request, input):
    context = {
        'Judul': 'Detail Artikel',
        'Heading': 'Halaman Detail Artikel: ' + input
    }
    return render(request, 'blog/index.html', context)


def spesial_artikel(request, inputInt):
    context = {
        'Judul': 'Spesial Artikel',
        'Heading': 'Spesial Artikel: ' + str(inputInt)
    }
    return render(request, 'blog/index.html', context)
