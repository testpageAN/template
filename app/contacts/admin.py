from django.contrib import admin  # noqa

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """Docstring for ContactAdmin."""
    list_display = (
        'id',
        'name',
        'listing',
        'email',
        'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing', 'contact_date')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
