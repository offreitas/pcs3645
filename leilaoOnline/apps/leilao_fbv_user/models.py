from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.urls import reverse
from django.conf import UserSettingsHolder, settings
from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

# import para fazer a comparacao com as tabelas fora de fbv_user (onde estao os cadastros)
from leilao_fbv.models import Vendedor as Vendedor_fbv
from leilao_fbv.models import Comprador as Comprador_fbv
from leilao_fbv.models import Leiloeiro as Leiloeiro_fbv

CATEGORY_CHOICES = (
    ('Administração, Negócios e Economia','Administração, Negócios e Economia'),
    ('Arte, Cinema e Fotografia', 'Arte, Cinema e Fotografia'),
    ('Artesanato, Casa e Estilo de Vida','Artesanato, Casa e Estilo de Vida'),
    ('Autoajuda','Autoajuda'),
    ('Biografias e Histórias Reais','Biografias e Histórias Reais'),
    ('Calendários e Anuários', 'Calendários e Anuários'),
    ('Ciências', 'Ciências'),
    ('Livro','Livro'),
    ('Computação, Informática e Mídias Digitais', 'Computação, Informática e Mídias Digitais'),
    ('Cristandade','Cristandade'),
    ('Crônicas, Humor e Entretenimento', 'Crônicas, Humor e Entretenimento'),
    ('Direito', 'Direito'),
    ('Educação', 'Educação'),
    ('Educação dos Filhos e Família', 'Educação dos Filhos e Família'),
    ('Educação, Referência e Didáticos', 'Educação, Referência e Didáticos'),
    ('Engenharia e Transporte', 'Engenharia e Transporte'),
    ('Esportes e Lazer', 'Esportes e Lazer'),
    ('Fantasia, Horror, e Ficção Científica', 'Fantasia, Horror, e Ficção Científica'),
    ('Gastronomia e Culinária', 'Gastronomia e Culinária'),
    ('História', 'História'),
    ('HQs, Mangás e Graphic Novels', 'HQs, Mangás e Graphic Novels'),
    ('Infantil', 'Infantil'),
    ('Jovens e Adolescentes', 'Jovens e Adolescentes'),
    ('LGBT', 'LGBT'),
    ('Literatura e Ficção', 'Literatura e Ficção'),
    ('Medicina', 'Medicina'),
    ('Policial, Suspense e Mistério', 'Policial, Suspense e Mistério'),
    ('Política, Filosofia e Ciências Sociais', 'Política, Filosofia e Ciências Sociais'),
    ('Preparação para Provas', 'Preparação para Provas'),
    ('Religião e Espiritualidade', 'Religião e Espiritualidade'),
    ('Romance', 'Romance'),
    ('Saúde e Família', 'Saúde e Família'),
    ('Turismo e Guias de Viagem', 'Turismo e Guias de Viagem'),
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

MONTH_CHOICES = (
    ('Mês', 'Mês'),
    ('Janeiro', 'Janeiro'),
    ('Fevereiro', 'Fevereiro'),
    ('Março', 'Março'),
    ('Abril', 'Abril'),
    ('Maio', 'Maio'),
    ('Junho', 'Junho'),
    ('Julho', 'Julho'),
    ('Agosto', 'Agosto'),
    ('Setembro', 'Setembro'),
    ('Outubro', 'Outubro'),
    ('Novembro', 'Novembro'),
    ('Dezembro', 'Dezembro'),
)
DAY_CHOICES = (
    ('Dia', 'Dia'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    ('31', '31'),
)

YEAR_CHOICES = (
    ('Ano', 'Ano'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024'),
    ('2025', '2025'),
    ('2026', '2026'),
    ('2027', '2027'),
)

LEILAO_CHOICES = (
    ("ATIVO", "Ativo"),
    ("FINALIZADO","Finalizado"),
    ("ESPERA", "Espera")
)

LOTE_CHOICES = (
    ('Pendente', 'Pendente'),
    ('Negado', 'Negado'),
    ('Aprovado', 'Aprovado'),
)

####################################################################################
### Lote ###########################################################################
####################################################################################

class Lote(models.Model):
    ### Para o vendedor preencher
    name = models.CharField(max_length=64, default='', blank=False)
    summary = models.CharField(max_length=512, default='', blank=False)
    quantity = models.IntegerField(default=1, blank=False)
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES, default='', blank=False)
    author = models.CharField(max_length=64, default='', blank=False)
    publisher = models.CharField(max_length=64, default='', blank=False)
    edition = models.CharField(max_length=64, default='', blank=False)
    number_of_pages = models.CharField(max_length=64, default='', blank=False)
    condition = models.CharField(max_length=64, choices=CONDITION_CHOICES, default='', blank=False)
    reserve_price = models.DecimalField(default=10.00, decimal_places=2, max_digits=16, blank=False)

    ### Para o leiloeiro preencher
    start_price = models.DecimalField(default=10.00, decimal_places=2, max_digits=16)
    minimum_bid = models.DecimalField(default=10.00, decimal_places=2, max_digits=16)
    state = models.CharField(max_length=16, choices=LOTE_CHOICES, default='Pendente')
    opening_month = models.CharField(max_length=16, choices=MONTH_CHOICES, default='Mês')
    opening_day = models.CharField(max_length=3, choices=DAY_CHOICES, default='Dia')
    opening_year = models.CharField(max_length=4, choices=YEAR_CHOICES, default='Ano')

    ### Preenchido automaticamente
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)
    
    def __str__(self):
        return self.name

    def set_user(self, user):
        self.user = user

    def get_absolute_url(self):
        return reverse('leilao_fbv_user:lote_edit', kwargs={'pk': self.pk})

class LoteForm(ModelForm):
    class Meta:
        model = Lote
        fields = ['name', 'summary', 'quantity', 'category',
                  'author', 'publisher', 'edition', 'number_of_pages',
                  'condition', 'reserve_price']

class LotePendingForm(ModelForm):
    class Meta:
        model = Lote
        fields = ['start_price', 'minimum_bid', 'state', 'opening_month',
                  'opening_day', 'opening_year']

class LoteDAO(models.Model):
    def lote_list(request, template_name):
        if request.user.is_staff:
            lote = Lote.objects.all()
        else:
            lote = Lote.objects.filter(user=request.user)
        data = {}
        data['object_list'] = lote
        return data

    def lote_list_pending(request, template_name):
        lote = Lote.objects.filter(state='Pendente')
        data = {}
        data['object_list'] = lote
        return data

    def available_list(request, template_name):
        lote = Lote.objects.filter(state='Aprovado')
        data = {}
        data['object_list'] = lote
        return data

    def lote_create(request, template_name):
        lote = Lote().set_user(request.user)
        form = LoteForm(request.POST or None)
        return form

    def lote_update(request, pk, template_name):
        if request.user.is_superuser:
            lote= get_object_or_404(Lote, pk=pk)
        else:
            lote= get_object_or_404(Lote, pk=pk, user=request.user)
        form = LoteForm(request.POST or None, instance=lote)
        return form

    def lote_delete(request, pk, template_name):
        if request.user.is_superuser:
            lote= get_object_or_404(Lote, pk=pk)
        else:
            lote= get_object_or_404(Lote, pk=pk, user=request.user)
        return lote

    def lote_pending(request, pk, template_name):
        lote = get_object_or_404(Lote, pk=pk)
        form = LotePendingForm(request.POST or None, instance=lote)
        return form, lote

        

####################################################################################
### Leilao #########################################################################
####################################################################################

class Leilao(models.Model):
    name = models.CharField(max_length=64, default='', blank=False)
    final_period = models.DateTimeField()
    status_leilao = models.CharField(max_length=16, choices=LEILAO_CHOICES, blank=False, null=False)

    lote = models.OneToOneField(
        Lote,
        on_delete=models.CASCADE,
    )

class LeilaoForm(ModelForm):
    class Meta:
        model = Leilao
        fields = ['name', 'final_period']

class LeilaoDAO(models.Model):
    def leilao_create(request, template_name):
        leilao = Leilao().set_user(request.user)
        form = LeilaoForm(request.POST or None)
        return form

    def leilao_delete(request, pk, template_name):
        if request.user.is_superuser:
            leilao= get_object_or_404(Lote, pk=pk)
        else:
            leilao= get_object_or_404(Lote, pk=pk, user=request.user)
        return leilao

    def leilao_update(request, pk, template_name):
        if request.user.is_superuser:
            leilao= get_object_or_404(Lote, pk=pk)
        else:
            leilao= get_object_or_404(Lote, pk=pk, user=request.user)
        form = LoteForm(request.POST or None, instance=leilao)
        return form

####################################################################################
### Lance ##########################################################################
####################################################################################

class Lance(models.Model):
    valor = models.FloatField()
    comprador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    leilao = models.ForeignKey(Leilao, on_delete=models.CASCADE)

    # Verificar isso depois
    def __str__(self):
        return '{0} - R${1}'.format(self.comprador.username, self.valor)

class LanceForm(ModelForm):
    class Meta:
        model = Lance
        fields = ['valor']

        
####################################################################################
### Leiloeiro ######################################################################
####################################################################################

class Leiloeiro(models.Model):
    name = models.CharField(max_length=256)
    username = models.CharField(max_length=16, default='', unique=True)
    email = models.CharField(max_length=256, default='', unique=True)
    password = models.CharField(max_length=16, default='')
    address = models.CharField(max_length=256)
    birth_date = models.DateField(default=date.today)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    bank = models.CharField(max_length=64, choices=BANK_CHOICES, default='')
    agency = models.IntegerField(default=1)
    account_number = models.CharField(max_length=64)
    salary = models.DecimalField(default=10, decimal_places=2, max_digits=8)
    
class LeiloeiroForm(ModelForm):
    class Meta:
        model = Leiloeiro
        fields = ['name', 'username','password',
                  'email','address', 'birth_date',
                  'rg', 'cpf', 'bank', 'agency',
                  'account_number', 'salary']

class LeiloeiroDAO(models.Model):
    def leiloeiro_list(request, template_name):
        lote = Leiloeiro.objects.all()
        data = {}
        data['object_list'] = lote
        return data
    
    def leiloeiro_create(request, template_name):
        form = LeiloeiroForm(request.POST or None)
        return form
    
    def leiloeiro_update(request, pk, template_name):
        leiloeiro = get_object_or_404(Leiloeiro, pk=pk)
        form = LoteForm(request.POST or None, instance=leiloeiro)
        return form

    def leiloeiro_delete(request, pk, template_name):
        leiloeiro = get_object_or_404(Leiloeiro, pk=pk)
        return leiloeiro

    def leiloeiro_filter(request, username):
        bool_user = Leiloeiro_fbv.objects.filter(username = username).exists()
        print("Entrou Username Leiloeiro filter", username, bool_user)
        return bool_user

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

    def vendedor_list(request, template_name):
        vendedor = Vendedor.objects.all()
        data = {}
        data['object_list'] = vendedor
        return data

    def vendedor_create(request, template_name):
        form = VendedorForm(request.POST or None)
        return form
    
    def vendedor_update(request, pk, template_name):
        vendedor = get_object_or_404(Vendedor, pk=pk)
        form = LoteForm(request.POST or None, instance=vendedor)
        return form

    def vendedor_delete(request, pk, template_name):
        vendedor = get_object_or_404(Vendedor, pk=pk)
        return vendedor
    
    def vendedor_filter(request, username):
        bool_user = Vendedor_fbv.objects.filter(username = username).exists()
        print("Entrou Username vendedor filter", username, bool_user)
        return bool_user

####################################################################################
### Comprador ######################################################################
####################################################################################

class Comprador(models.Model):
    name = models.CharField(max_length=256)
    username = models.CharField(max_length=16, default='')
    email = models.CharField(max_length=256, default='')
    password = models.CharField(max_length=16, default='')
    address = models.CharField(max_length=256)
    birth_date = models.DateField(default=date.today)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    card_number = models.CharField(max_length=16, default='')
    
class CompradorForm(ModelForm):
    class Meta:
        model = Comprador
        fields = ['name', 'username', 'email', 'password',
                  'address', 'birth_date', 'rg',
                  'cpf', 'card_number']

class CompradorDAO(models.Model):

    def comprador_list(request, template_name):
        comprador = Comprador.objects.all()
        data = {}
        data['object_list'] = comprador
        return data

    def comprador_create(request, template_name):
        form = CompradorForm(request.POST or None)
        return form
    
    def comprador_update(request, pk, template_name):
        comprador = get_object_or_404(Comprador, pk=pk)
        form = LoteForm(request.POST or None, instance=comprador)
        return form

    def comprador_delete(request, pk, template_name):
        comprador = get_object_or_404(Comprador, pk=pk)
        return comprador

    def comprador_filter(request, username):
        bool_user = Comprador_fbv.objects.filter(username = username).exists()
        print("Entrou Username comprador filter", username, bool_user)
        return bool_user

####################################################################################
### Leilao #########################################################################
####################################################################################

# class Leilao(models.Mode):
#     name = models.CharField(max_length=64, default='', blank=False)
#     summary = models.CharField(max_length=512, default='', blank=False)
#     quantity = models.IntegerField(default=1, blank=False)
#     category = models.CharField(max_length=64, choices=CATEGORY_CHOICES, default='', blank=False)
#     author = models.CharField(max_length=64, default='', blank=False)
#     publisher = models.CharField(max_length=64, default='', blank=False)
#     edition = models.CharField(max_length=64, default='', blank=False)
#     number_of_pages = models.CharField(max_length=64, default='', blank=False)
#     condition = models.CharField(max_length=64, choices=CONDITION_CHOICES, default='', blank=False)
#     reserve_price = models.DecimalField(default=10.00, decimal_places=2, max_digits=16, blank=False)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)

####################################################################################
### WIP: Relatorio #################################################################
####################################################################################

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