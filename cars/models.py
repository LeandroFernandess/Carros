"""
Car Models Module

Este módulo define os modelos para representar uma marca de carro e um carro, além do inventário
de carros na aplicação. Eles são usados para gerenciar informações e manter o registro atualizado
de veículos no sistema.

Dependências:
-------------
- django.db.models: Biblioteca de ORM do Django utilizada para definir os modelos
"""

from django.db import models


class Brand(models.Model):
    """
    Classe para representar uma Marca de carro.

    Atributos:
        id (AutoField): Identificador único para a marca.
        name (CharField): Nome da marca, com até 200 caracteres.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        """
        Retorna a representação em string da marca, que é o nome da marca.

        Returns:
            str: Nome da marca.
        """
        return self.name


class Car(models.Model):
    """
    Classe para representar um Carro.

    Atributos:
        id (AutoField): Identificador único para o carro.
        model (CharField): Nome do modelo do carro.
        brand (ForeignKey): Referência à marca do carro.
        factory_year (IntegerField): Ano de fabricação do carro.
        model_year (IntegerField): Ano do modelo do carro.
        plate (CharField): Placa do carro.
        value (FloatField): Valor do carro.
        photo (ImageField): Foto do carro.
        bio (TextField): Biografia do carro, gerada automaticamente.
    """

    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand")
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to="cars/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Retorna a representação em string do carro, que é o modelo do carro.

        Returns:
            str: Modelo do carro.
        """
        return self.model


class CarInventory(models.Model):
    """
    Modelo que representa o inventário de carros.

    Atributos:
        cars_count (IntegerField): Número de carros no inventário.
        cars_value (FloatField): Valor total dos carros no inventário.
        created_at (DateTimeField): Data e hora de criação do registro.
    """

    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Metadados para o modelo CarInventory.

        Atributos:
            ordering (list): Define a ordenação padrão para as consultas.
        """

        ordering = ["-created_at"]

    def __str__(self):
        """
        Retorna a representação em string do objeto CarInventory.

        Returns:
            str: Número de carros e valor total do inventário.
        """
        return f"{self.cars_count} - {self.cars_value}"
