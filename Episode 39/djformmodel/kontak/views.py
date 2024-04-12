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
    f_kontak = KontakForm(request.POST or None)
    salah = None
    if request.method == 'POST':
        if f_kontak.is_valid():
            #! queryset ORM
            Kontak.objects.create(
                nama=f_kontak.cleaned_data.get('nama'),
                email=f_kontak.cleaned_data.get('email'),
                pesan=f_kontak.cleaned_data.get('pesan'),
            )
            return HttpResponseRedirect("/kontak/")
        else:
            salah = f_kontak.errors
    context = {
        'Judul': 'Kirim pesan',
        'Heading': 'Kirim Pesan',
        'f_kontak': f_kontak,
        'salah': salah,
    }
    return render(request, 'kontak/create.html', context)
