from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

# import models & frosm
from . models import Tujuan
from . forms import TujuanForm


def update(request, nm_slug):
    obj = Tujuan.objects.get(slug=nm_slug)
    if request.method == 'POST':
        form = TujuanForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil di update')
            return redirect('pulangpergi:index')
    else:
        form = TujuanForm(instance=obj)
    context = {
        'Judul': 'Tambah Daftar Tujuan',
        'Heading': 'Tambah Daftar Tujuan',
        'form': form,
    }
    return render(request, 'pulangpergi/update.html', context)


def delete(request, nm_slug):
    Tujuan.objects.filter(slug=nm_slug).delete()
    messages.success(request, 'Data berhasil di hapus')
    return redirect('pulangpergi:index')


def add_tujuan(request):
    if request.method == 'POST':
        form = TujuanForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil di tambahkan')
            return redirect('pulangpergi:index')
    else:
        form = TujuanForm()
    context = {
        'Judul': 'Tambah Daftar Tujuan',
        'Heading': 'Tambah Daftar Tujuan',
        'form': form,
    }
    return render(request, 'pulangpergi/create.html', context)


def index(request):
    semua_tujuan = Tujuan.objects.all()
    context = {
        'Judul': 'Daftar Tujuan',
        'Heading': 'Daftar Tujuan',
        'semua_tujuan': semua_tujuan,
    }
    return render(request, 'pulangpergi/index.html', context)
