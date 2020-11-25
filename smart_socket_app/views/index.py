from django.shortcuts import render

from smart_socket_app.forms.login import LogInForm
from smart_socket_app.models import LogInProfile


def index(request):
    if LogInProfile.objects.exists():
        # profile = Profile.objects.all()[0]
        # expenses = Expense.objects.all()
        # expenses_cost = sum(expense.price for expense in expenses)
        # profile.budget_left = profile.budget - expenses_cost
        # context = {
        #     'profile': profile,
        #     'expenses': expenses,
        # }
        # return render(request, 'home-with-profile.html', context)
        return render(request, 'home.html')
    else:
        context = {
            'form': LogInForm()
        }
        return render(request, 'index.html', context)
