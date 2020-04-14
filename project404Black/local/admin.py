from django.contrib import admin
from .models import Local

class FielsEdit(admin.ModelAdmin):
    list_display = ('logradouro', 'numero')

admin.site.register(Local, FielsEdit)
