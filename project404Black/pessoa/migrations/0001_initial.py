# Generated by Django 3.0.5 on 2020-04-12 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('local', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=50, null=True, verbose_name='nome')),
                ('cnpj', models.CharField(db_index=True, max_length=15, unique=True, verbose_name='CNPJ')),
                ('cpf', models.CharField(db_index=True, max_length=15, unique=True, verbose_name='CPF')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='data de nascimento')),
                ('celular', models.CharField(blank=True, max_length=14, null=True, verbose_name='celular')),
                ('telefone', models.CharField(blank=True, max_length=11, null=True, verbose_name='telefone')),
                ('local', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='local.Local', verbose_name='endereço')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]