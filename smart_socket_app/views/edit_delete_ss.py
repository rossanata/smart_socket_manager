from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from smart_socket_app.forms import SmartSocketForm
from smart_socket_app.models import SmartSocket


@login_required
def edit_ss(request, pk, action=''):
    smart_socket = SmartSocket.objects.get(pk=pk)
    if smart_socket.owner != request.user:
        return redirect('index')
    if request.method == 'GET':
        if action == 'delete':
            smart_socket.delete()
            return redirect('index')
        context = {
            'smart_socket': smart_socket,
            'form': SmartSocketForm(instance=smart_socket)
        }
        return render(request, 'edit_ss.html', context)

    else:
        form = SmartSocketForm(request.POST, instance=smart_socket)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'smart_socket': smart_socket,
            'form': form,
        }
    return render(request, 'edit_ss.html', context)

