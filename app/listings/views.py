from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger  # noqa

from django.views.generic.detail import DetailView  # noqa
from .choices import foreman_choices, type_choices

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
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    """Docstring"""

    context = {
        'foreman_choices': foreman_choices,
        'type_choices': type_choices,
    }
    return render(request, 'listings/search.html', context)


# class ListingDetailView(DetailView):
#     model = Listing
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
