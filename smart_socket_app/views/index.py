from django.shortcuts import render
from smart_socket_app.models import SmartSocket

# def YOUR_VIEW_DEF(request, pk):
#     YOUR_OBJECT.objects.filter(pk=pk).update(views=F('views')+1)
#     return HttpResponseRedirect(request.GET.get('next')))


def index(request, socket_name='', cmd=''):
    if request.user.is_authenticated:
        current_owner_sockets = SmartSocket.objects.filter(owner=request.user)
        # sockets = SmartSocket.objects.all()
        # current_owner_sockets = []
        # for socket in sockets:
        #     if request.user == socket.owner:
        #         current_owner_sockets.append(socket)
        context = {
            'owner_sockets': current_owner_sockets,
            'user': request.user,
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
