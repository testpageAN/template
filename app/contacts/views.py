from django.http import HttpResponse  # noqa
from django.shortcuts import redirect
from django.contrib import messages

from .models import Contact


def contact(request):
    """Docstring for contact."""
    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')
        listing = request.POST.get('listing')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        user_id = request.POST.get('user_id')
        foreman_email = request.POST.get('foreman_email')  # noqa

        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message, user_id=user_id,
            # foreman_email=foreman_email
        )

        contact.save()

        messages.success(request, 'Your message has been submitted')
        return redirect('/listings/' + listing_id)
