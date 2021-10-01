# Generated by Django 3.2.7 on 2021-10-01 22:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leilao_fbv_user', '0003_auto_20211001_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lote',
            name='user',
        ),
        migrations.AlterField(
            model_name='lote',
            name='category',
            field=models.CharField(choices=[('automotivo_peças', 'Automotivos e Peças'), ('beleza', 'Beleza e Cuidados Pessoais'), ('esportes', 'Esporte'), ('brinquedos', 'Brinquedos e Jogos'), ('cozinha', 'Cozinha'), ('eletronicos', 'Eletronicos'), ('games e consoles', 'Games e Console'), ('livros', 'Livro'), ('papelaria', 'Papelaria e Escritório'), ('petshop', 'Pet Shop'), ('vestuario', 'Roupas Calçados e Acessórios')], default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='lote',
            name='condition',
            field=models.CharField(choices=[('novo', 'NOVO'), ('usado', 'USADO')], default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='lote',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='lote',
            name='opening_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='lote',
            name='qty',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='lote',
            name='summary',
            field=models.CharField(default='', max_length=512),
        ),
    ]
