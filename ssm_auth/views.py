# from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from ssm_auth.forms import RegisterUserForm, LogInForm, ProfileForm


@transaction.atomic
def register_user(request):
    if request.method == 'GET':
        context = {
            'user_form': RegisterUserForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, 'auth/register_user.html', context)

    else:
        user_form = RegisterUserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('index')
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'auth/register_user.html', context)


def login_user(request):
    errors = ''
    if request.method == 'GET':
        context = {
            'login_form': LogInForm(),
        }
        return render(request, 'auth/log_in.html', context)
    else:
        login_form = LogInForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('index')
            else:
                errors = "* username or password not valid"
        context = {
            'login_form': login_form,
            'errors': errors,
        }
        return render(request, 'auth/log_in.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('index')


@login_required
def edit_delete_user(request, pk, action=""):
    current_user = User.objects.get(pk=pk)
    if current_user != request.user:
        return redirect('index')
    if request.method == 'GET':
        if action == 'delete':
            current_user.delete()
            return redirect('index')
        context = {
            'current_user': current_user,
            'user_form': RegisterUserForm(instance=current_user)
        }
        return render(request, 'auth/edit_user.html', context)

    else:
        form = RegisterUserForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            login(request, current_user)
            return redirect('index')

        context = {
            'current_user': current_user,
            'form': form,
        }
    return render(request, 'auth/edit_user.html', context)


