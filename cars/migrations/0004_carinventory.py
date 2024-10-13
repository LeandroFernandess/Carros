"""
Migração do Django para criar o modelo `CarInventory`.

Detalhes da mudança:
--------------------
1. Criação do modelo `CarInventory`:
   - Atributos:
     - `id`: BigAutoField, chave primária automática.
     - `cars_count`: IntegerField, armazena a quantidade de carros.
     - `cars_value`: FloatField, armazena o valor total dos carros.
     - `created_at`: DateTimeField, armazena a data de criação, preenchida automaticamente ao adicionar.

2. Configuração de Ordenação:
   - Os registros são ordenados por `created_at` em ordem decrescente.

Autores:
--------
- Django 5.0.7: Geração automática em 19 de setembro de 2024.
"""

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0003_car_photo_car_plate"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarInventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cars_count", models.IntegerField()),
                ("cars_value", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
