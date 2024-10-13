"""
Migração do Django para o aplicativo 'cars'.

Detalhes da mudança:
--------------------
1. Adição de Campo:
   - Modelo: `Car`
   - Campo: `bio` (TextField, permite vazio e nulo)

Dependências:
-------------
- Requer a migração `0004_carinventory` do aplicativo `cars`.

Autores:
--------
- Django 5.0.7: Geração automática em 19 de setembro de 2024.
"""

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0004_carinventory"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
    ]
