from django.shortcuts import render

from .models import Listing


def index(request):
    """Docstring"""
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    """Docstring"""
    return render(request, 'listings/listing.html')


def search(request):
    """Docstring"""
    return render(request, 'listings/search.html')
