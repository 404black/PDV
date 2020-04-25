from django.db import models
from pessoa.models import Fornecedor

class Compra(models.Model):
    data_compra = models.DateField('data da compra', null=True, blank=True)
    hora_compra = models.DateField('hora da compra', null=True, blank=True)
    data_pagamento = models.DateField('data de pagamento', null=True, blank=True)
    valor_total_compra = models.CharField('valor total da compra',  max_length=16, null=True, blank=True)
    fornecedor = models.ForeignKey(Fornecedor, verbose_name="fornecedor", null=True, blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        if self.fornecedor:
            return 'Fornecedor que estamos comprando: ' + self.fornecedor.nome
        return str(self.id)
    