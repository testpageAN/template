from django.shortcuts import render

from listings.models import Listing
from foremen.models import Foreman

from listings.choices import foreman_choices, type_choices


def index(request):
    """Docstring"""
    listings = (
        Listing.objects.order_by('next_check')
        .filter(is_active=True)[:10]
    )

    context = {
        'listings': listings,
        'foreman_choices': foreman_choices,
        'type_choices': type_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    """Docstring"""
    # Get all foremen
    foremen = Foreman.objects.order_by('-hire_date')

    context = {
        'foremen': foremen,
        # 'mvp_foremen': mvp_foremen  # If any
    }
    return render(request, 'pages/about.html', context)
