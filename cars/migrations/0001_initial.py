"""
Migração do Django para criação do modelo 'Car'

Esta migração inicial cria a tabela `Car` com os campos definidos.

Autores:
--------
- Django 5.0.7: Geração automática em 14 de agosto de 2024.

Campos Criados:
---------------
- id: Chave primária automática.
- model: Nome do modelo do carro (CharField).
- brand: Marca do carro (CharField).
- factory_year: Ano de fabricação (IntegerField), opcional.
- model_year: Ano do modelo (IntegerField), opcional.
- value: Valor do carro (FloatField), opcional.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("model", models.CharField(max_length=200)),
                ("brand", models.CharField(max_length=200)),
                ("factory_year", models.IntegerField(blank=True, null=True)),
                ("model_year", models.IntegerField(blank=True, null=True)),
                ("value", models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
