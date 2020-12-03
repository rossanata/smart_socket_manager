from django.contrib.auth.models import User
from django.shortcuts import render

from smart_socket_app.forms import SmartSocketForm
from smart_socket_app.models import SmartSocket
from ssm_auth.models import LogInUser


def index(request):
    if LogInUser.objects.exists():
        # profile = Profile.objects.all()[0]
        # expenses = Expense.objects.all()
        # expenses_cost = sum(expense.price for expense in expenses)
        # profile.budget_left = profile.budget - expenses_cost
        # context = {
        #     'profile': profile,
        #     'expenses': expenses,
        # }
        # return render(request, 'home-with-profile.html', context)
        return render(request, 'index.html')
    else:
        context = {
            'sockets': SmartSocket.objects.all(),
            'user': request.user,
        }
        return render(request, 'index.html', context)
