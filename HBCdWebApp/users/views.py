from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, UserCreationForm


def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # print('Hello POST!')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('home')

        # either form not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        # print('Not valid!')
        return render(request, 'users/login.html', {'form': form})


def sign_out(request):
    """
    :param request:
    :return:
    """
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('home')


def signup(request):
    """
    """
    context = {'form': UserCreationForm()}

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        # else:
        # print(form.errors)  # Check errors when testing as needed.
    return render(request, "users/signup.html", context)
