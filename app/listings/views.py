from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator  # noqa

from .models import Listing


def index(request):
    """Docstring"""
    listings = Listing.objects.order_by('next_check').filter(is_active=True)

    paginator = Paginator(listings, 5)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    """Docstring"""
    return render(request, 'listings/listing.html')


def search(request):
    """Docstring"""
    return render(request, 'listings/search.html')
