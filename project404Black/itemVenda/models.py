from django.db import models
from venda.models import Venda
from produto.models import Produto

class ItemVenda(models.Model):
    qtd_item = models.IntegerField("quantidade item")
    valor_item = models.FloatField("valor item", max_length=15,default=0)
    venda = models.ForeignKey(Venda, verbose_name="venda", on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, verbose_name="produto", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'item de venda'
        verbose_name_plural = 'itens de vendas'
        
    def get_produto(self, calcular=False):
        if calcular:
            return self.produto.descricao + " no valor de: " + self.qtd_item * self.valor_item
        return self.produto.descricao 

    def __str__(self):
        if self.produto:
            return 'Produto: ' +  self.produto.descricao 
        return str(self.id)
