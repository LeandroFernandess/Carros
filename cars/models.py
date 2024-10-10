"""
Este módulo define modelos para uma aplicação de gerenciamento de carros.

Includes:
    - Brand: Representa uma marca de carro.
    - Car: Representa um carro com vários atributos, incluindo uma relação com a marca.
    - CarInventory: Representa um inventário de carros.
"""

from django.db import models


class Brand(models.Model):
    """
    Classe para representar uma Marca de carro.
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
        cars_count (int): Número de carros no inventário.
        cars_value (float): Valor total dos carros no inventário.
        created_at (datetime): Data e hora de criação do registro.
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
