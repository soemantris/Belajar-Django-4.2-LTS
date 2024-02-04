from django.shortcuts import render

# Create your views here.
from .models import Artikel


def index(request):
    articles = Artikel.objects.all()
    category = Artikel.objects.values('kategori__nama').distinct()
    context = {
        'Judul': 'Blog',
        'Heading': 'Halaman Blog',
        'Articles': articles,
        'Categories': category,
    }
    return render(request, 'blog/index.html', context)


def detail_artikel(request, slugInput):
    detail_articles = Artikel.objects.get(slug_art=slugInput)
    context = {
        'Judul': 'Detail Blog',
        'Heading': 'Halaman Detail Blog',
        'DetailArtikel': detail_articles,
    }
    return render(request, 'blog/detail.html', context)
