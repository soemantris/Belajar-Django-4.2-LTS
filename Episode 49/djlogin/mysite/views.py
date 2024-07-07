from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# import forms register user
from . forms import RegisterUserForm


def register_user(request):

    if request.method == 'POST':
        register_user = RegisterUserForm(request.POST or None)
        if register_user.is_valid():
            messages.success(request, 'Selamat berhasil registrasi!')
            register_user.save()
            return redirect('index')
        else:
            messages.error(request, 'Gagal registrasi!')
            return redirect('register')
    else:
        register_user = RegisterUserForm()

    context = {
        'judul': 'Register User',
        'form': register_user,
    }
    return render(request, 'register.html', context)


def index(request):
    context = {
        'judul': 'Beranda',
    }

    print(request.user.is_authenticated)

    return render(request, 'index.html', context)


def login_user(request):
    context = {
        'judul': 'Login',
    }

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')

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


@login_required(login_url='/')
def logout_user(request):
    context = {
        'judul': 'Logout',
    }

    # if request.method == 'GET':
    #     if not request.user.is_authenticated:
    #         return redirect('index')

    if request.method == 'POST':
        # print(request.POST)
        if request.POST['keluar'] == 'Logout':
            logout(request)
            messages.info(request, 'Berhasil keluar!')
            # print('sedang proses keluar')
            return redirect('index')

    return render(request, 'logout.html', context)
