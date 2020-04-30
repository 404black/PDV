from django.db import models

INATIVO = 1
ATIVO = 2

STATUS = [
(1, 'INATIVO'),
(2, 'ATIVO'),
]

class Produto(models.Model):
    descricao = models.CharField("descricao", max_length=101)
    quantidade = models.IntegerField("quantidade")
    valor_compra = models.FloatField("valor compra", max_length=16)
    valor_venda = models.FloatField("valor venda", max_length=15)
    _status = models.PositiveIntegerField("status",  choices=STATUS,default=ATIVO)

    class Meta:
        ordering = ('descricao',)
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'
        
    def __str__(self):
        if self.descricao:
            return 'Produto: ' +  self.descricao 
        return str(self.id)

    @property
    def status(self):
        for code, label in STATUS:
            if self._status == code:
                break
        return label
        
    @status.setter
    def status(self, status):
        if status == 'Inativo':
            self._status = INATIVO
        elif status == 'Ativo':
            self._status = ATIVO
        else:
            raise valueError('Escolha entre: Inativo ou Ativo')