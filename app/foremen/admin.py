from django.contrib import admin
from .models import Foreman


class ForemanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',
                    'is_our', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Foreman, ForemanAdmin)
