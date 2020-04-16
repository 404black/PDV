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
    funcionario = models.ForeignKey(Funcionario, verbose_name="funcionario",null=True, blank=True,on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, verbose_name="cliente",on_delete=models.CASCADE)

    class Meta:
        ordering = ('data_venda',)
        verbose_name = 'venda'
        verbose_name_plural = 'vendas'
        
    def __str__(self):
        if self.data_venda:
            return 'Data da Venda: ' +  self.data_venda + ', Cliente: ' + self.cliente.nome
        return str(self.id)



