from django.shortcuts import render


def index(request):

    context = {
        'Judul': 'Home',
        'Heading': 'Django Forms',
    }

    if request.method == 'POST':
        print('ini post punya')
        context['nama'] = request.POST['nama']
        context['email'] = request.POST['email']
    else:
        print('ini get punya')

    return render(request, 'index.html', context)
