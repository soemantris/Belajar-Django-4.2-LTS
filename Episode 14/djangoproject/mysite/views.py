from django.shortcuts import render

def index(request):
    context = {
        'title':'portopolio',
        'subtitle':'selamat datang di channel ini good peoples, terima kasih sudah subscribe!',
        'banner':'images/beranda.png',
    }
    return render(request, 'index.html', context)