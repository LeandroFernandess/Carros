# Gerado por Django 5.0.7 em 2024-09-19 22:07

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Migração para criar o modelo CarInventory.

    Esta migração cria um novo modelo chamado CarInventory, que mantém o controle
    da quantidade e valor dos carros, juntamente com o timestamp de criação.
    """

    dependencies = [
        ("cars", "0003_car_photo_car_plate"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarInventory",
            fields=[
                # Chave primária para o modelo, gerada automaticamente.
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                # Campo inteiro para armazenar a quantidade de carros.
                ("cars_count", models.IntegerField()),
                # Campo float para armazenar o valor total dos carros.
                ("cars_value", models.FloatField()),
                # Campo DateTime para armazenar a data de criação, configurado automaticamente.
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                # Ordena pela data de criação em ordem decrescente.
                "ordering": ["-created_at"],
            },
        ),
    ]
