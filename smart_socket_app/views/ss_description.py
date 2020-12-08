import required as required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from smart_socket_app.forms import SmartSocketForm
from smart_socket_app.models import SmartSocket


@login_required
def ss_description(request, pk):
    ss = SmartSocket.objects.get(pk=pk)
    if ss.owner != request.user:
        return redirect('index')
    form = SmartSocketForm(instance=ss)
    if request.method == 'GET':
        context = {
            'smart_socket': ss,
            'form': form,
        }
        return render(request, 'ss_description.html', context)
