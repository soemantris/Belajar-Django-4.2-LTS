from django.shortcuts import render

# Create your views here.

from . models import Artikel


def index(request):
    return render(request, 'index.html', {'title': 'blog', 'headline': 'selamat datang di halaman blog'})


def kategori(request, kategoriInput):
    category = Artikel.objects.filter(kategori=kategoriInput)
    context = {
        'title': 'kategori',
        'headline': 'artikel berdasarkan kategori',
        'categories': category,
    }
    return render(request, 'blog/kategori.html', context)


def detail_artikel(request, slugInput):
    articles = Artikel.objects.get(slug=slugInput)
    context = {
        'title': 'detail artikel',
        'headline': 'ini halaman detail artikel',
        'articles': articles,
    }
    return render(request, 'blog/detail_artikel.html', context)
