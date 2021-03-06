# Generated by Django 3.0.5 on 2020-04-12 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(blank=True, max_length=255, null=True, verbose_name='endereço')),
                ('numero', models.CharField(blank=True, max_length=10, null=True, verbose_name='número')),
                ('complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='complemento')),
                ('bairro', models.CharField(blank=True, max_length=255, null=True, verbose_name='bairro')),
                ('cidade', models.CharField(blank=True, max_length=255, null=True, verbose_name='cidade')),
                ('estado', models.CharField(blank=True, max_length=2, null=True, verbose_name='estado')),
                ('cep', models.CharField(blank=True, max_length=9, null=True, verbose_name='cep')),
                ('geocode', models.CharField(blank=True, max_length=32, null=True, verbose_name='geolocalização (lat,lng)')),
                ('criado_em', models.DateTimeField(editable=False, verbose_name='data de criação')),
                ('editado_em', models.DateTimeField(blank=True, null=True, verbose_name='última atualização')),
            ],
            options={
                'verbose_name': 'local',
                'verbose_name_plural': 'locais',
                'ordering': ('logradouro',),
            },
        ),
    ]
