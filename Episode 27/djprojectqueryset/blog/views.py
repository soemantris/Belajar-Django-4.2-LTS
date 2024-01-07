from django.shortcuts import render

# Create your views here.
from .models import Artikel


def index(request):
    semuaArtikel = Artikel.objects.order_by('-judul')
    print(semuaArtikel)
    context = {
        'title': 'blog',
        'headline': 'selamat datang di halaman blog',
        'articles': semuaArtikel
    }
    return render(request, 'index.html', context)


def kategori_blog(request):
    semuaArtikel = Artikel.objects.filter(kategori__nama='blog')
    context = {
        'title': 'blog',
        'headline': 'selamat datang di halaman blog',
        'articles': semuaArtikel
    }
    return render(request, 'index.html', context)


def berita(request):
    semuaArtikel = Artikel.objects.filter(kategori__nama='berita')
    context = {
        'title': 'blog',
        'headline': 'selamat datang di halaman blog berita',
        'articles': semuaArtikel
    }
    return render(request, 'index.html', context)


def bukan_gibah(request):
    semuaArtikel = Artikel.objects.exclude(kategori__nama='gibah')
    context = {
        'title': 'blog',
        'headline': 'selamat datang di halaman blog gibah',
        'articles': semuaArtikel
    }
    return render(request, 'index.html', context)
