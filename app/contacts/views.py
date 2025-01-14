from django.http import HttpResponse  # noqa
from django.shortcuts import redirect
from django.contrib import messages

from .models import Contact

from django.core.mail import send_mail


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
        foreman_email = request.POST.get('foreman_email')

        # Check if email sender has already sent email for the same instr.
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = (
                Contact.objects.all().
                filter(listing_id=listing_id, user_id=user_id)
            )
            if has_contacted:
                messages.error(
                    request,
                    'You have already informed about this instrument'
                )
                return redirect('/listings/' + listing_id)

        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message, user_id=user_id,
        )

        contact.save()

        send_mail(
            "Subject here",
            "Here is the message for " + listing + '. Sign in for more info.',
            "my_gmail_mail",
            [foreman_email, 'my_real_email'],
            fail_silently=False,
        )

        messages.success(request, 'Your message has been submitted')
        return redirect('/listings/' + listing_id)
