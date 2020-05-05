from django.db import models
from pessoa.models import Funcionario
from pessoa.models import Cliente
from django.utils import timezone

CREDITO = 1;
DEBITO = 2;
DINHEIRO = 4;
CHEQUE = 4;

FORMA_PAGAMENTO = [
(1, 'CRÉDITO'),
(2, 'DÉBITO'),
(3, 'DINHEIRO'),
(4, 'CHEQUE'),
]

class Venda(models.Model):
    data_venda = models.DateField('data da venda', null=True, blank=True)
    hora_venda = models.DateField('hora venda', null=True, blank=True)
    data_pagamento = models.DateField('data de pagamento', null=True, blank=True)
    valor_total_venda = models.CharField('valor total da venda',  max_length=16, null=True, blank=True)
    _forma_pagamento = models.PositiveIntegerField('forma de pagamento',  choices=FORMA_PAGAMENTO,default=DINHEIRO)
    funcionario = models.ForeignKey(Funcionario, verbose_name="funcionario",null=True, blank=True,on_delete=models.SET_NULL)
    cliente = models.ForeignKey(Cliente, verbose_name="cliente", null=True, blank=True,on_delete=models.SET_NULL)

    class Meta:
        ordering = ('data_venda',)
        verbose_name = 'venda'
        verbose_name_plural = 'vendas'
        
    def __str__(self):
        if self.cliente:
            return 'Venda par o Cliente: ' + self.cliente.nome
        return str(self.id)

    @property
    def forma_pagamento(self):
        for code, label in FORMA_PAGAMENTO:
            if self._forma_pagamento == code:
                break
        return label
        
    @forma_pagamento.setter
    def forma_pagamento(self, valor):
        if valor == 'Crédito':
            self._forma_pagamento = CREDITO
        elif valor == 'Débito':
            self._forma_pagamento = DEBITO
        elif valor == 'Dinheiro':
            self._forma_pagamento = DINHEIRO
        elif valor == 'Cheque':
            self._forma_pagamento = CHEQUE
        else:
            raise valueError('Escolha entre: Crédito, Débito, Dinheiro ou Cheque')



