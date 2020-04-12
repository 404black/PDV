from django.db import models
from django.utils import timezone

class Local(models.Model):
    logradouro = models.CharField("endereço", max_length=255, null=True, blank=True)
    numero = models.CharField("número", max_length=10, blank=True, null=True)
    complemento = models.CharField("complemento", max_length=100, blank=True, null=True)
    bairro = models.CharField("bairro",max_length=255, null=True, blank=True)
    cidade = models.CharField("cidade", max_length=255, null=True, blank=True)
    estado = models.CharField("estado", max_length=2, null=True, blank=True)
    cep = models.CharField("cep", max_length=9, null=True, blank=True)
    geocode = models.CharField("geolocalização (lat,lng)", max_length=32, null=True, blank=True)
    criado_em = models.DateTimeField("data de criação", editable=False)
    editado_em = models.DateTimeField("última atualização", null=True, blank=True)

    class Meta:
        ordering = ('logradouro',)
        verbose_name = 'local'
        verbose_name_plural = 'locais'
    def _str_(self):
        if self.logradouro and self.numero:
            return self.logradouro + ', ' + self.numero
        return str(self.id)
    def save(self, *args, **kwargs):
        if not self.criado_em:
            self.criado_em = timezone.now()
        self.editado_em = timezone.now()
        return super(Local, self).save(*args, **kwargs)
