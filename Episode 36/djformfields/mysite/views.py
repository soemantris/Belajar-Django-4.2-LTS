from django.shortcuts import render

from .forms import FormFields

def index(request):
    form_fields = FormFields()
    context = {
        'Judul':'Beranda',
        'Heading':'Form Fields',
        'form_fields': form_fields,
    }
    return render(request, 'index.html', context)
