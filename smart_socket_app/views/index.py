from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from paho.mqtt import publish
from smart_socket_app.models import SmartSocket


def index(request, socket_name='', cmd=''):
    if request.user.is_authenticated:
        current_owner_sockets = SmartSocket.objects.filter(owner=request.user)
        paginator = Paginator(current_owner_sockets, 6)
        page_number = request.GET.get('page', 1)
        # try:
        sockets = paginator.get_page(page_number)
        # except EmptyPage:
        #     sockets = None

        if socket_name and cmd:
            for socket in current_owner_sockets:
                if socket_name == socket.name:
                    current_socket_unique_address = request.user.username + '/' + socket_name
                    publish.single(current_socket_unique_address + "/cmnd/POWER", cmd, hostname="192.168.1.6")

        context = {
            'owner_sockets': current_owner_sockets,
            'user': request.user,
            "sockets": sockets,
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
