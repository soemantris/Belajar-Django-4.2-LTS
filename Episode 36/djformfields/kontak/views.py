from django.shortcuts import render

from .forms import KontakForms

# Create your views here.
def index(request):
    kontak_forms = KontakForms()
    context = {
        'Judul':'Kontak',
        'Heading':'Kontak Forms',
        'kontak_form': kontak_forms,
    }
    print(request.POST)
    return render(request, 'kontak/index.html', context)
