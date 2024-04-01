from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
# ? import forms kontak
from .forms import KontakForm

# ? import models kontak
from .models import KontakModel as Kontak


def index(request):
    #! queryset ORM
    contacts = Kontak.objects.all().order_by('-waktu_kirim')
    context = {
        'Judul': 'Kontak',
        'Heading': 'Daftar Kontak Masuk',
        'contacts': contacts,
    }
    return render(request, 'kontak/index.html', context)


def create(request):
    f_kontak = KontakForm()
    if request.method == 'POST':
        #! queryset ORM
        Kontak.objects.create(
            nama=request.POST.get('nama'),
            email=request.POST.get('email'),
            pesan=request.POST.get('pesan'),
        )
        return HttpResponseRedirect("/kontak/")
    context = {
        'Judul': 'Kirim pesan',
        'Heading': 'Kirim Pesan',
        'f_kontak': f_kontak,
    }
    return render(request, 'kontak/create.html', context)
