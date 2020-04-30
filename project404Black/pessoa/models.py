from django.db import models
from django.utils import timezone
from local.models import Local

MASCULINO = 1
FEMININO = 2

SEXO = [
(1, 'MASCULINO'),
(2, 'FEMININO'),
]

class Pessoa(models.Model):
    nome = models.CharField("nome", max_length=51, null=True, blank=True)
    cnpj = models.CharField("CNPJ", unique=True, db_index=True, max_length=15, null=True, blank=True)
    cpf = models.CharField("CPF", unique=True, db_index=True, max_length=15, null=True, blank=True)
    data_nascimento = models.DateField('data de nascimento', null=True, blank=True)
    celular = models.CharField("celular", max_length=14, null=True, blank=True)
    local = models.OneToOneField(Local, verbose_name="endereço", on_delete=models.CASCADE,null=True, blank=True)
    _sexo = models.PositiveIntegerField("sexo", choices=SEXO,default=MASCULINO)

    class Meta:
        abstract = True

    def __str__(self):
        if self.nome:
            return self.nome
        return str(self.id)

    @property
    def endereco_completo(self):
        return self.local.__str__()

    @property
    def sexo(self):
        for code, label in SEXO:
            if self._sexo == code:
                break
        return label
        
    @sexo.setter
    def sexo(self, sexo):
        if sexo == 'Masculino':
            self._sexo = MASCULINO
        elif sexo == 'Feminino':
            self._sexo = FEMININO
        else:
            raise valueError('Escolha entre: Masculino ou Feminino')

class Cliente(Pessoa):
    data_cadastro = models.DateField('Data de Cadastro')
    
    class Meta:
        ordering = ('nome',)
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
    # vamos sobreescrever o método __str__() usando herança
    def __str__(self):
        return super().__str__()

class Fornecedor(Pessoa):
    data_cadastro = models.DateField('Data de Cadastro')
    status = models.CharField('Status', max_length=10)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'fornecedor'
        verbose_name_plural = 'fornecedores'
    # vamos sobreescrever o método __str__() usando herança
    def __str__(self):
        return super().__str__()

class Funcionario(Pessoa):
    data_entrada = models.DateField('Data de Entrada', null=True,blank=True)
    data_saida = models.DateField('Data de Saida', null=True,blank=True)
    usuario = models.CharField('Usuario', max_length=30, null=True, blank=True)
    senha = models.CharField('Senha', max_length=30, null=True, blank=True)
    nivel_acesso = models.CharField('Nivel de Acesso', max_length=50)
    status = models.CharField('Status', max_length=10)
    
    class Meta:
        ordering = ('nome',)
        verbose_name = 'funcionario'
        verbose_name_plural = 'funcionarios'
    # vamos sobreescrever o método __str__() usando herança
    def __str__(self):
        return super().__str__()
