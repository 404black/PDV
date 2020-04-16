from django.contrib import admin
from .models import Produto

class FielsEdit(admin.ModelAdmin):
    list_display = ('descricao', 'quantidade')

admin.site.register(Produto, FielsEdit)