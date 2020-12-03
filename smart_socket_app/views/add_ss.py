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
            # ss_address = request.user.id + request.name
            ss_form.save()
            return redirect('index')
        context = {
            'ss_form': ss_form,
            # 'user': User(),
        }
        return render(request, 'add_ss.html', context)
