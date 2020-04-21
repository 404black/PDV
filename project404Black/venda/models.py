from django.db import models
from pessoa.models import Funcionario
from pessoa.models import Cliente
from django.utils import timezone

class Venda(models.Model):
    data_venda = models.DateField('data da venda', null=True, blank=True)
    hora_venda = models.DateField('hora venda', null=True, blank=True)
    data_pagamento = models.DateField('data de pagamento', null=True, blank=True)
    valor_total_venda = models.CharField('valor total venda',  max_length=16, null=True, blank=True)
    forma_pagamento = models.CharField('forma de pagamento',  max_length=10, null=True, blank=True)
    funcionario = models.ForeignKey(Funcionario, verbose_name="funcionario",null=True, blank=True,on_delete=models.SET_NULL)
    cliente = models.ForeignKey(Cliente, verbose_name="cliente", null=True, blank=True,on_delete=models.SET_NULL)

    class Meta:
        ordering = ('data_venda',)
        verbose_name = 'venda'
        verbose_name_plural = 'vendas'
        
    def __str__(self):
        if self.cliente:
            return 'Cliente que esta vendendo: ' + self.cliente.nome
        return str(self.id)



