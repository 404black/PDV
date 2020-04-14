from django.contrib import admin
from .models import Pessoa

class FielsEdit(admin.ModelAdmin):
    list_display = ('nome', 'telefone')

admin.site.register(Pessoa, FielsEdit)
