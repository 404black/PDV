from django.contrib import admin
from .models import Venda

class FielsEdit(admin.ModelAdmin):
    list_display = ('data_venda', 'valor_total_venda')

admin.site.register(Venda, FielsEdit)