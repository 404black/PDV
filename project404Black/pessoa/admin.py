from django.contrib import admin
from .models import Fornecedor
from .models import Cliente
from .models import Funcionario

class FielsEdit(admin.ModelAdmin):
    list_display = ('nome', 'celular')

admin.site.register(Funcionario, FielsEdit)
admin.site.register(Fornecedor, FielsEdit)
admin.site.register(Cliente, FielsEdit)
