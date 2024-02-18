from django.shortcuts import render


def index(request):
    context = {
        'Judul': 'Home',
        'Heading': 'Halo semuanya dan selamat datang teman-teman'
    }
    return render(request, 'index.html', context)
