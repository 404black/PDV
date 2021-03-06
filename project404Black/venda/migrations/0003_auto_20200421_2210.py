# Generated by Django 3.0.5 on 2020-04-21 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0010_auto_20200421_2210'),
        ('venda', '0002_auto_20200416_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pessoa.Cliente', verbose_name='cliente'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='funcionario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pessoa.Funcionario', verbose_name='funcionario'),
        ),
    ]
