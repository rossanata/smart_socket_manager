from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from smart_socket_app.forms import SmartSocketForm


def add_ss(request):
    if request.method == 'GET':
        context = {
            'ss_form': SmartSocketForm(),
        }
        return render(request, 'add_ss.html', context)

    else:
        ss_form = SmartSocketForm(request.POST)
        if ss_form.is_valid():
            ss_form = ss_form.save(commit=False)
            ss_form.owner = request.user
            ss_form.unique_address = request.user.username + '/' + ss_form.name
            ss_form.save()
            return redirect('index')
        context = {
            'ss_form': ss_form,
        }
        return render(request, 'add_ss.html', context)
