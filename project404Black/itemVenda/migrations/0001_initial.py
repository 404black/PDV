# Generated by Django 3.0.5 on 2020-04-16 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0002_auto_20200416_1840'),
        ('venda', '0002_auto_20200416_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd_item', models.FloatField(max_length=15, verbose_name='quantidade item')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.Produto', verbose_name='produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venda.Venda', verbose_name='venda')),
            ],
            options={
                'verbose_name': 'item de venda',
                'verbose_name_plural': 'itens de vendas',
            },
        ),
    ]
