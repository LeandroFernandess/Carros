"""
Django Management Script

Este script configura o ambiente Django e executa comandos de linha de comando utilizando o utilitário 
`django.core.management.execute_from_command_line`. É uma parte essencial na administração de projetos 
Django, permitindo a realização de diversas tarefas administrativas.

Dependências:
-------------
- os: Biblioteca padrão para interações com o sistema operacional.
- sys: Biblioteca padrão para manipulação de argumentos e interação com o interpretador Python.
- django.core.management: Módulo do Django contendo utilitários para gerenciamento de projeto.
"""

import os
import sys


def main():
    """
    Configura o ambiente para Django e executa comandos de linha de comando.

    Define a variável de ambiente `DJANGO_SETTINGS_MODULE` com as configurações
    do projeto Django e então executa `execute_from_command_line` com os
    argumentos fornecidos via linha de comando.

    Levanta:
        ImportError: Se o Django não estiver instalado ou configurado corretamente,
        o que pode ocorrer se as dependências não estiverem instaladas ou se um ambiente
        virtual não estiver ativado.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar o Django. Você tem certeza de que ele está "
            "instalado e disponível na variável de ambiente PYTHONPATH? Você "
            "esqueceu de ativar um ambiente virtual?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
