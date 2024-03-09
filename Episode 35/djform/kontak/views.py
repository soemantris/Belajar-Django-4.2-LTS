from django.shortcuts import render


# Create your views here.
# ? Membuat class form

from django import forms

class KontakForm(forms.Form):
    nama = forms.CharField()
    email = forms.EmailField()
    subjek = forms.CharField()
    pesan = forms.CharField()

def index(request):
    kontak_form = KontakForm()
    context = {
        'Judul': 'Kontak',
        'Heading': 'Kontak Forms',
        'kontak_form': kontak_form,
    }
    if request.method == 'POST':
        print('ini post punya kontak')
        context['nama'] = request.POST['nama']
        context['email'] = request.POST['email']
        context['subjek'] = request.POST['subjek']
        context['pesan'] = request.POST['pesan']
    else:
        print('ini get punya kontak')
    return render(request, 'kontak/index.html', context)
