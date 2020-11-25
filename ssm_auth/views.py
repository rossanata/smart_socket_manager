from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


def login_view(request):
    username = 'rossana'
    password = '12345qwe'
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return redirect('index')
    return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')

