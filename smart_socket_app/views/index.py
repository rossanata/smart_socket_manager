from django.core.paginator import Paginator
from django.shortcuts import render
from paho.mqtt import publish

from smart_socket_app.forms import FilterForm
from smart_socket_app.models import SmartSocket


def index(request, socket_name='', cmd=''):
    search_query = request.GET.get('search', '')
    if request.user.is_authenticated:
        current_owner_sockets = SmartSocket.objects.filter(owner=request.user).order_by('name')
        current_owner_sockets_filtered = current_owner_sockets.filter(name__icontains=search_query)

        paginator = Paginator(current_owner_sockets_filtered, 5)
        page_number = request.GET.get('page', 1)
        sockets = paginator.get_page(page_number)

        if socket_name and cmd:
            for socket in current_owner_sockets:
                if socket_name == socket.name:
                    current_socket_unique_address = request.user.username + '/' + socket_name
                    publish.single(current_socket_unique_address + "/cmnd/POWER", cmd, hostname="192.168.1.5")

        context = {
            'owner_has_sockets': True if current_owner_sockets else False,
            'sockets_to_list': current_owner_sockets_filtered,
            'user': request.user,
            "sockets": sockets,
            'form': FilterForm(initial={'search': search_query}),
            'search': search_query
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
