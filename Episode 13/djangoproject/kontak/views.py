from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'kontak',
        'subtitle':'ini adalah halaman kontak hubungi atau krim email di sumsyahrul@gmail.com',
        'banner':'kontak/images/kontak.png',
    }
    return render(request, 'index.html', context)