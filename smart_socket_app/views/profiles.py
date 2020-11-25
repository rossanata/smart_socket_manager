from django.shortcuts import render, redirect

from smart_socket_app.forms.login import LogInForm


def home(request):
    return render(request, 'home.html')


def create_profile(request):
    if request.method == 'GET':
        context = {
            'form': LogInForm(),
        }

        return render(request, 'index.html')
    else:
        form = LogInForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        context = {
            'form': form,
        }

        return render(request, 'index.html', context)
