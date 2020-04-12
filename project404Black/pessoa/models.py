from django.db import models
from django.utils import timezone
from local.models import Local

class Pessoa(models.Model):
    nome = models.CharField("nome", max_length=50, null=True, blank=True)
    cnpj = models.CharField("CNPJ", unique=True, db_index=True, max_length=15, null=True, blank=True)
    cpf = models.CharField("CPF", unique=True, db_index=True, max_length=15, null=True, blank=True)
    data_nascimento = models.DateField('data de nascimento', null=True, blank=True)
    celular = models.CharField("celular", max_length=14, null=True, blank=True)
    telefone = models.CharField("telefone", max_length=11, null=True, blank=True)
    local = models.OneToOneField(Local, verbose_name="endereço", on_delete=models.CASCADE,
    null=True, blank=True)

    class Meta:
        abstract = False

    def _str_(self):
        if self.nome:
            return self.nome
        return str(self.id)

    def get_endereco(self):
        return self.local._str_()
