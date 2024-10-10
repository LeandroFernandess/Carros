"""
Configuração do aplicativo 'accounts'.

Este módulo contém a classe de configuração da aplicação 'accounts'. Ele define parâmetros importantes
para o comportamento do aplicativo no projeto Django.

Classes:
    - AccountsConfig: Configurações específicas para o aplicativo 'accounts'. Define o campo padrão
      para chaves primárias de modelos e o nome do aplicativo.

Dependências:
    - django.apps.AppConfig: Classe base para configurações de aplicativos no Django.
"""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Classe de configuração para o aplicativo 'accounts'.

    Atributos:
        default_auto_field (str): Define o campo padrão para chave primária em novos modelos.
        name (str): Nome do aplicativo.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"
