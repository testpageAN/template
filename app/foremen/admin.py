from django.contrib import admin
from .models import Foreman

admin.site.register(Foreman, admin.ModelAdmin)
