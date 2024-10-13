"""
Cars Application Configuration Module

Este módulo configura a aplicação 'cars' no projeto Django, definindo
atributos essenciais e atividades a serem realizadas quando a aplicação estiver pronta.

Dependências:
-------------
- django.apps.AppConfig: Classe base para configurar uma aplicação Django.
"""

from django.apps import AppConfig


class CarsConfig(AppConfig):
    """
    Configuração da aplicação 'cars'.

    Atributos:
        default_auto_field (str): Tipo de campo de chave primária padrão.
        name (str): Nome da aplicação.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "cars"

    def ready(self):
        """
        Método chamado quando a aplicação Django está pronta.

        Importa o módulo de sinais da aplicação 'cars'.
        """
        import cars.signals
