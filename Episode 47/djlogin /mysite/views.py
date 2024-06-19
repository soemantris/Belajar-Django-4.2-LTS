from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    context = {
        'judul': 'Beranda',
    }
    return render(request, 'index.html', context)


def login_user(request):
    context = {
        'judul': 'Login',
    }

    if request.method == 'POST':
        username_input = request.POST['username']
        password_input = request.POST['password']

        user = authenticate(request, username=username_input,
                            password=password_input)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login berhasil')
            return redirect('index')
        else:
            messages.error(request, 'Login gagal!')
            return redirect('login')

    # username_user = 'admin'
    # password_user = '123'
    # user = authenticate(username=username_user, password=password_user)
    # login(request, user)

    return render(request, 'login.html', context)


def logout_user(request):
    context = {
        'judul': 'Logout',
    }

    if request.method == 'POST':
        # print(request.POST)
        if request.POST['keluar'] == 'Logout':
            logout(request)
            messages.info(request, 'Berhasil keluar!')
            # print('sedang proses keluar')
            return redirect('index')

    return render(request, 'logout.html', context)
