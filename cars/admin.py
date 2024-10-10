"""
Configuração do Django Admin para os modelos Car e Brand.

Includes:
    - BrandAdmin: Configuração de exibição e busca para o modelo Brand.
    - CarAdmin: Configuração de exibição e busca para o modelo Car.
"""

from django.contrib import admin
from cars.models import Car, Brand


class BrandAdmin(admin.ModelAdmin):
    """
    Configuração do Django Admin para o modelo Brand.

    Atributos:
        list_display (tuple): Campos a serem exibidos na lista de marcas.
        search_fields (tuple): Campos a serem usados para buscas.
    """

    list_display = ("name",)
    search_fields = ("name",)


class CarAdmin(admin.ModelAdmin):
    """
    Configuração do Django Admin para o modelo Car.

    Atributos:
        list_display (tuple): Campos a serem exibidos na lista de carros.
        search_fields (tuple): Campos a serem usados para buscas.
    """

    list_display = (
        "model",
        "brand",
        "factory_year",
        "model_year",
        "value",
    )
    search_fields = ("model", "brand")


# Registro dos modelos Car e Brand no site de administração.
admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
