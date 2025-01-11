from django.shortcuts import render


def index(request):
    """Docstring"""
    return render(request, 'listings/listings.html')


def listing(request):
    """Docstring"""
    return render(request, 'listing/listing.html')


def search(request):
    """Docstring"""
    return render(request, 'listings/search.html')
