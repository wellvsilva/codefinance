# coding: utf-8

from django.db import models

SITUACAOCONTA_CHOICE = (
    ('PA', 'PAGA'),
    ('PE', 'PENDENTE'),
    ('AT', 'ATRASADA'),
    ('CA', 'CANCELADA'),
    ('PO', 'PRORROGADA'),
)


class TipoDocumento(models.Model):
    '''
    Tipos de Documentos: Nota fiscal, Cupom fiscal, Cupom Nao fiscal,  etc...
    '''
    descricao =  models.CharField(max_length=100)

    def __unicode__(self):
        return self.descricao


class TipoDespesa(models.Model):
    '''
    Tipos de Despesas: SAE, Bandeirantes, Cantao de Credito, Supermercado, Combustivel, Escola, etc...
    '''
    descricao = models.CharField(max_length=100)

    def __unicode__(self):
        return self.descricao


class FormaPagamento(models.Model):
    '''
    Forma de Pagamento: Cartao de Credito, Cartao de Debito, Debito em Conta, Cheque, Dinheiro, etc...
    '''
    descricao = models.CharField(max_length=100)

    def __unicode__(self):
        return self.descricao


class ContaPagar(models.Model):
    descricao = models.CharField(max_length=255)
    tipo_despesa = models.ForeignKey('TipoDespesa', related_name='contapagar_tipodespesa')
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField()
    numero_documento = models.CharField(max_length=50) # 50 porque pensei na posssibilidade de adicionar uma chave NFe
    tipo_documento = models.ForeignKey('TipoDocumento',related_name='contapagar_tipodocumento')
    situaca = models.CharField(max_length=2, choices=SITUACAOCONTA_CHOICE, default='PE')
    valor_conta = models.DecimalField(max_digits=12, decimal_places=2)
    desconto = models.DecimalField(max_digits=12, decimal_places=2)
    multa = models.DecimalField(max_digits=12, decimal_places=2)
    juros = models.DecimalField(max_digits=12, decimal_places=2)
    valor_pago = models.DecimalField(max_digits=12, decimal_places=2)
    forma_pagamento = models.ForeignKey('FormaPagamento', related_name='contapagar_formapagamento')
    observacoes = models.TextField()

    def __unicode__(self):
        return self.descricao


class Banco(models.Model):
    codigo = models.CharField(max_length=3)
    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return self.codigo
CHEQUEORIGIEM_CHOICE = (
    ('P', 'PROPRIO'),
    ('T', 'TERCEIRO'),
)

AVISTAPRE_CHOICE = (
    ('A', 'A VISTA'),
    ('P', u'Pré Datado'),
)


SITUACAOCHEQUE_CHOICE = (
    ('CU', 'EM CUSTODIA'),
    ('CO', 'COMPENSADO'),
    ('DE', 'DEPOSITADO'),
)


class Cheque(models.Model):
    banco = models.ForeignKey('Banco', related_name='cheque_banco')
    cmc7 = models.CharField(max_length=100)
    origem = models.CharField(max_length=1, choices=CHEQUEORIGIEM_CHOICE, default='P')
    dados_terceiro = models.TextField()
    avista_pre = models.CharField(max_length=1, choices=AVISTAPRE_CHOICE, default='A')
    data_pre = models.DateField(null=True, blank=True)
    situacao = models.CharField(max_length=2, choices=SITUACAOCHEQUE_CHOICE, default='C')
    conta = models.ForeignKey('ContaPagar', related_name='cheque_contapagar')
    valor = models.DecimalField(max_digits=12, decimal_places=2)

    def __unicode__(self):
        return self.banco





