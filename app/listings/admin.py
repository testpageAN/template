from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'description',
                    'type', 'lrv', 'urv',
                    'units', 'manufacturer',
                    'is_active', 'foreman',
                    'interval', 'last_checked',
                    'next_check')
    list_display_links = ('id', 'tag')
    list_filter = ('next_check',)
    list_editable = ('is_active',)
    search_fields = ('tag', 'type')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
