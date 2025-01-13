from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    """Docstring"""
    if request.method == 'POST':
        #  Register User
        messages.error(request, 'Testing error messages')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    """Docstring"""
    if request.method == 'POST':
        #  Login User
        pass
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    """Docstring"""
    return redirect('index')


def dashboard(request):
    """Docstring"""
    return render(request, 'accounts/dashboard.html')
