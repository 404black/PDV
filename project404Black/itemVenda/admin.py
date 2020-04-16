from django.contrib import admin
from .models import ItemVenda

class FielsEdit(admin.ModelAdmin):
    list_display = ('produto','qtd_item','valor_item')

admin.site.register(ItemVenda, FielsEdit)