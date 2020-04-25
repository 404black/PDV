from django.db import models
from compra.models import Compra
from produto.models import Produto

class ItemCompra(models.Model):
    qtd_item = models.IntegerField("quantidade do item")
    valor_item = models.FloatField("valor do item", max_length=15,default=0)
    produto = models.ForeignKey(Produto, verbose_name="produto", on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, verbose_name="compra", on_delete=models.CASCADE)

    def __str__(self):
        if self.produto:
            return 'Produto: ' +  self.produto.descricao 
        return str(self.id)




