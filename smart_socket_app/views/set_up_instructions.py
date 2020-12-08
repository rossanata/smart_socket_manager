from django.shortcuts import render


def set_up_instructions(request):
    return render(request, 'set_up_instructions.html')