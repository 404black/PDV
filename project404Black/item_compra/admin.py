from django.contrib import admin
from .models import ItemCompra

class FielsEdit(admin.ModelAdmin):
    list_display = ('produto','qtd_item','valor_item')

admin.site.register(ItemCompra, FielsEdit)