"""
Configuração da aplicação 'cars' no Django.

Módulos:
    cars.apps: Inclui a classe de configuração da aplicação.

Classes:
    CarsConfig: Configurações específicas para a aplicação de carros.
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
