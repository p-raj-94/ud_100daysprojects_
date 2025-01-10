from django.contrib import admin
from .models import Cafe


class CafeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'has_sockets', "has_wifi")
    search_fields = ['name']

# Register your models here.
admin.site.register(Cafe, CafeAdmin)
