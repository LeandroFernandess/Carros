"""
Migração do Django para criar o modelo `Brand` e alterar o campo `brand` no modelo `Car`.

Esta migração faz duas alterações principais:
1. Criação da tabela `Brand` com um campo de nome.
2. Atualização do campo `brand` no modelo `Car` para ser uma chave estrangeira referenciando `Brand`.

Autores:
--------
- Django 5.0.7: Geração automática em 15 de agosto de 2024.

Alterações:
-----------
1. Criação do Modelo `Brand`:
   - id: Chave primária automática.
   - name: Nome da marca (CharField).

2. Alteração no Modelo `Car`:
   - brand: Modificado para chave estrangeira, referenciando `Brand`, com deleção protegida.
"""

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name="car",
            name="brand",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="car_brand",
                to="cars.brand",
            ),
        ),
    ]
