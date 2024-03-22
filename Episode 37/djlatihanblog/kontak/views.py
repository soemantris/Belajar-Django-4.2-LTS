from django.shortcuts import render

# Create your views here.
from .forms import KontakForms


def index(request):
    kontak_form = KontakForms()
    context = {
        'Judul': 'Kontak',
        'Heading': 'Kontak Forms',
        'f_kontak': kontak_form,
    }
    print(request.POST)
    return render(request, 'kontak/index.html', context)
