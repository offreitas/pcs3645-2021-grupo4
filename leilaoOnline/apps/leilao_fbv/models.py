from django.db import models
from django.urls import reverse
from apps import settings
from datetime import date
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.apps import apps

CATEGORY_CHOICES = (
    ('Automotivos e Peças','Automotivos e Peças'),
    ('Beleza e Cuidados Pessoais', 'Beleza e Cuidados Pessoais'),
    ('Esporte','Esporte'),
    ('Brinquedos e Jogos','Brinquedos e Jogos'),
    ('Cozinha','Cozinha'),
    ('Eletrônicos', 'Eletrônicos'),
    ('Games e Consoles', 'Games e Consoles'),
    ('Livro','Livro'),
    ('Papelaria e Escritório', 'Papelaria e Escritório'),
    ('Pet Shop','Pet Shop'),
    ('Roupas Calçados e Acessórios', 'Roupas Calçados e Acessórios'),
)

CONDITION_CHOICES = (
    ('Novo','Novo'),
    ('Usado','Usado'),
)

BANK_CHOICES = (
    ('Itau Unibanco S.A.','Itau Unibanco S.A.'),
    ('Banco do Brasil S.A.', 'Banco do Brasil S.A.'),
    ('Banco Bradesco S.A.','Banco Bradesco S.A.'),
    ('Caixa Economica Federal','Caixa Economica Federal'),
    ('Banco Santander (Brasil) S.A.','Banco Santander (Brasil) S.A.'),
    ('NuBank', 'NuBank'),
    ('C6','C6'),
    ('Banco Inter S.A.', 'Banco Inter S.A.'),
)

####################################################################################
### Lote ###########################################################################
####################################################################################

# Lote = apps.get_model('leilao_fbv_user', 'Lote')

# class Lote(models.Model):
#     lote_fbv_user = models.ForeignKey('leilao_fbv_user.Lote')

# class Lote(models.Model):
#     name = models.CharField(max_length=200, default='')
#     summary = models.CharField(max_length=512, default='')
#     qty = models.IntegerField(default=1)
#     category = models.CharField(max_length=64, choices=CATEGORY_CHOICES, default='')
#     condition = models.CharField(max_length=64, choices=CONDITION_CHOICES, default='')
#     min_value = models.DecimalField(default=10.00, decimal_places=2, max_digits=16)
#     opening_date = models.DateField(default=date.today)
#     # Como atriubiu user sem usar o campo de formulario???????
#     user = models.CharField(max_length=256, editable=True, default='')

#     def __str__(self):
#         return self.name

#     def set_user(self, user):
#         self.user = user

#     def get_absolute_url(self):
#         return reverse('leilao_fbv_user:lote_edit', kwargs={'pk': self.pk})

# class LoteForm(ModelForm):
#     class Meta:
#         model = Lote
#         fields = ['name', 'summary', 'qty',
#                   'category', 'condition', 'min_value',
#                   'opening_date', 'user']

# class LoteDAO(models.Model):
    
#     def lote_list(request, template_name):
#         lote = Lote.objects.all()
#         data = {}
#         data['object_list'] = lote
#         return data

    # def lote_create(request, template_name, user_arg):
    #     lote = Lote().set_user(user_arg)
    #     form = LoteForm(request.POST or None, instance=lote)
    #     # form = LoteForm(request.POST or None)
    #     return form

    # def lote_update(request, pk, template_name):
    #     lote = get_object_or_404(Lote, pk=pk)
    #     form = LoteForm(request.POST or None, instance=lote)
    #     return form

    # def lote_delete(request, pk, template_name):
    #     lote = get_object_or_404(Lote, pk=pk)    
    #     return lote

# ####################################################################################
# ### Leiloeiro ######################################################################
# ####################################################################################

# class Leiloeiro(models.Model):
#     name = models.CharField(max_length=256)
#     address = models.CharField(max_length=256)
#     birth_date = models.DateField(default=date.today)
#     rg = models.CharField(max_length=9)
#     cpf = models.CharField(max_length=11)
#     bank = models.CharField(max_length=64, choices=BANK_CHOICES, default='')
#     agency = models.IntegerField(default=1)
#     account_number = models.CharField(max_length=64)
#     salary = models.DecimalField(default=10, decimal_places=2, max_digits=8)
    
# class LeiloeiroForm(ModelForm):
#     class Meta:
#         model = Leiloeiro
#         fields = ['name', 'address', 'birth_date',
#                   'rg', 'cpf', 'bank', 'agency',
#                   'account_number', 'salary']

# class LeiloeiroDAO(models.Model):
#     def leiloeiro_list(request, template_name):
#         lote = Leiloeiro.objects.all()
#         data = {}
#         data['object_list'] = lote
#         return data
    
#     def leiloeiro_create(request, template_name):
#         form = LeiloeiroForm(request.POST or None)
#         return form
    
#     def leiloeiro_update(request, pk, template_name):
#         leiloeiro = get_object_or_404(Leiloeiro, pk=pk)
#         form = LoteForm(request.POST or None, instance=leiloeiro)
#         return form

#     def leiloeiro_delete(request, pk, template_name):
#         leiloeiro = get_object_or_404(Leiloeiro, pk=pk)
#         return leiloeiro

####################################################################################
### Vendedor #######################################################################
####################################################################################

class Vendedor(models.Model):
    name = models.CharField(max_length=256)
    username = models.CharField(max_length=16, default='')
    email = models.CharField(max_length=256, default='')
    password = models.CharField(max_length=16, default='')
    address = models.CharField(max_length=256)
    birth_date = models.DateField(default=date.today)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    bank = models.CharField(max_length=64, choices=BANK_CHOICES, default='')
    agency = models.IntegerField(default=1)
    account_number = models.CharField(max_length=64)
    
class VendedorForm(ModelForm):
    class Meta:
        model = Vendedor
        fields = ['name', 'username', 'email', 'password',
                  'address', 'birth_date', 'rg',
                  'cpf', 'bank', 'agency',
                  'account_number']

class VendedorDAO(models.Model):

    # def vendedor_list(request, template_name):
    #     vendedor = Vendedor.objects.all()
    #     data = {}
    #     data['object_list'] = vendedor
    #     return data

    def vendedor_create(request, template_name):
        form = VendedorForm(request.POST or None)
        return form
    
    # def vendedor_update(request, pk, template_name):
    #     vendedor = get_object_or_404(Vendedor, pk=pk)
    #     form = LoteForm(request.POST or None, instance=vendedor)
    #     return form

    # def vendedor_delete(request, pk, template_name):
    #     vendedor = get_object_or_404(Vendedor, pk=pk)
    #     return vendedor

# ####################################################################################
# ### Comprador ######################################################################
# ####################################################################################

# class Comprador(models.Model):
#     name = models.CharField(max_length=256)
#     address = models.CharField(max_length=256)
#     birth_date = models.DateField(default=date.today)
#     rg = models.CharField(max_length=9)
#     cpf = models.CharField(max_length=11)
#     bank = models.CharField(max_length=64, choices=BANK_CHOICES, default='')
#     agency = models.IntegerField(default=1)
#     account_number = models.CharField(max_length=64)
    
# class CompradorForm(ModelForm):
#     class Meta:
#         model = Comprador
#         fields = ['name', 'address', 'birth_date',
#                   'rg', 'cpf', 'bank', 'agency',
#                   'account_number']

# class CompradorDAO(models.Model):

#     def comprador_list(request, template_name):
#         comprador = Comprador.objects.all()
#         data = {}
#         data['object_list'] = comprador
#         return data

#     def comprador_create(request, template_name):
#         form = CompradorForm(request.POST or None)
#         return form
    
#     def comprador_update(request, pk, template_name):
#         comprador = get_object_or_404(Comprador, pk=pk)
#         form = LoteForm(request.POST or None, instance=comprador)
#         return form

#     def comprador_delete(request, pk, template_name):
#         comprador = get_object_or_404(Comprador, pk=pk)
#         return comprador
        
# ####################################################################################
# ### WIP: Relatorio #################################################################
# ####################################################################################

# class Relatorio(models.Model):
#     leilao = models.IntegerField(default=1)
#     lote = models.CharField(max_length=256)
#     vendas = models.CharField(max_length=256)
#     receita = models.CharField(max_length=256)
#     custos = models.CharField(max_length=256)
#     lucro = models.CharField(max_length=256)
#     periodo = models.DateField(default=date.today)
#     vendedor = models.CharField(max_length=256)
#     comprador = models.CharField(max_length=256)
#     lances = models.CharField(max_length=256)
#     vencedor = models.CharField(max_length=256)