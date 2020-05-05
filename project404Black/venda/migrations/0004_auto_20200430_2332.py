# Generated by Django 3.0.5 on 2020-04-30 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0003_auto_20200421_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='forma_pagamento',
        ),
        migrations.AddField(
            model_name='venda',
            name='_forma_pagamento',
            field=models.PositiveIntegerField(choices=[(1, 'CRÉDITO'), (2, 'DÉBITO'), (3, 'DINHEIRO'), (4, 'CHEQUE')], default=4, verbose_name='forma de pagamento'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='valor_total_venda',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='valor total da venda'),
        ),
    ]
