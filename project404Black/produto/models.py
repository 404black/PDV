from django.db import models

class Produto(models.Model):
    descricao = models.CharField("descricao", max_length=101)
    quantidade = models.IntegerField("quantidade")
    valor_compra = models.FloatField("valor compra", max_length=16)
    valor_venda = models.FloatField("valor venda", max_length=15)
    status = models.CharField("status",  max_length=15)

    class Meta:
        ordering = ('descricao',)
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'
        
    def __str__(self):
        if self.descricao:
            return 'Produto: ' +  self.descricao 
        return str(self.id)