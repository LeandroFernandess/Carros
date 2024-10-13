"""
Migração do Django para adicionar campos `photo` e `plate` ao modelo `Car`.

Esta migração faz as seguintes alterações no modelo `Car`:
1. Adição de um campo `photo` para armazenar imagens.
2. Adição de um campo `plate` para armazenar a placa do carro.

Autores:
--------
- Django 5.0.7: Geração automática em 16 de agosto de 2024.

Alterações:
-----------
1. Campo `photo`:
   - Tipo: ImageField.
   - Opções: `upload_to` configurado para "cars/", permitido nulo e em branco.

2. Campo `plate`:
   - Tipo: CharField.
   - Opções: Máximo de 10 caracteres, permitido nulo e em branco.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0002_brand_alter_car_brand"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="cars/"),
        ),
        migrations.AddField(
            model_name="car",
            name="plate",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
