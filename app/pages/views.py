from django.shortcuts import render


def index(request):
    """Docstring"""
    return render(request, 'pages/index.html')


def about(request):
    """Docstring"""
    return render(request, 'pages/about.html')
