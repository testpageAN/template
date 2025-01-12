from django.shortcuts import render, redirect


def register(request):
    """Docstring"""
    return render(request, 'accounts/register.html')


def login(request):
    """Docstring"""
    return render(request, 'accounts/login.html')


def logout(request):
    """Docstring"""
    return redirect('index')


def dashboard(request):
    """Docstring"""
    return render(request, 'accounts/dashboard.html')
