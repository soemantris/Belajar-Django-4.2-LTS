from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

# import models & frosm
from . models import Tujuan
from . forms import TujuanForm


def update(request, nm_slug):
    # obj_tujuan = Tujuan.objects.get(slug=nm_slug)

    obj_tujuan = get_object_or_404(Tujuan, slug=nm_slug)

    if request.method == 'POST':
        form = TujuanForm(request.POST or None, instance=obj_tujuan)

        if form.is_valid():
            form.save()
            return redirect('pulangpergi:index')

    else:
        form = TujuanForm(instance=obj_tujuan)

    context = {
        'Judul': 'Edit Daftar Tujuan',
        'Heading': 'Edit Daftar Tujuan',
        'form': form,
    }

    return render(request, 'pulangpergi/update.html', context)


def delete(request, nm_slug):
    Tujuan.objects.filter(slug=nm_slug).delete()
    return redirect('pulangpergi:index')


def add_tujuan(request):

    if request.method == 'POST':
        form = TujuanForm(request.POST or None)
        if form.is_valid():
            form.save()
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
