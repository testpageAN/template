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
    queryset_list = (
        Listing.objects.order_by('next_check')
        .filter(is_active=True)
    )

    # Tag
    if 'tag' in request.GET:
        tag = request.GET.get('tag')
        if tag:
            queryset_list = queryset_list.filter(tag__icontains=tag)

    # Type
    if 'type' in request.GET:
        type = request.GET.get('type')
        if type:
            queryset_list = queryset_list.filter(type__icontains=type)

    # Foreman
    if 'foreman' in request.GET:
        foreman = request.GET.get('foreman')
        if foreman:
            queryset_list = queryset_list.filter(foreman__name__iexact=foreman)

    context = {
        'foreman_choices': foreman_choices,
        'type_choices': type_choices,
        'listings': queryset_list,
        'values': request.GET,
    }
    return render(request, 'listings/search.html', context)
