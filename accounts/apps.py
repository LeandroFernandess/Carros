"""
Configuração do aplicativo 'accounts' para um projeto Django.

Descrição:
----------
Este módulo especifica a configuração padrão do aplicativo 'accounts'.

Classe:
-------
- AccountsConfig: Configurações específicas para o aplicativo 'accounts', incluindo o tipo de chave primária padrão e o nome do aplicativo.

Atributos da Classe:
--------------------
- default_auto_field (str): Especifica o campo padrão para chaves primárias em novos modelos ('BigAutoField').
- name (str): Nome do aplicativo ('accounts').

Autores:
--------
- Configuração gerada com base na estrutura do Django.
"""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Configurações do aplicativo 'accounts'."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"
