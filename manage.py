#!/usr/bin/env python
"""
Django Management Utility Script

Este script é utilizado como ponto de entrada para executar tarefas administrativas em 
um projeto Django, como migrações de banco de dados, execução de servidores de desenvolvimento, 
e outras funcionalidades fornecidas pelo Django através da linha de comando.

Dependências:
-------------
- Django: Este script depende do framework Django, que deve estar instalado e disponível 
  na variável de ambiente `PYTHONPATH`. Caso o Django não esteja instalado, o script lançará 
  uma exceção `ImportError`.
- Variável de ambiente `DJANGO_SETTINGS_MODULE`: O módulo de configuração do Django deve ser 
  especificado como `app.settings` ou o nome equivalente do seu projeto.

Fluxo de Execução:
------------------
1. Define a variável de ambiente `DJANGO_SETTINGS_MODULE`, que especifica o caminho para as 
   configurações do projeto Django.
2. Tenta importar o módulo `execute_from_command_line` do pacote `django.core.management`.
3. Caso a importação falhe, lança uma exceção explicando possíveis problemas, como Django 
   não estar instalado ou a falta de um ambiente virtual ativado.
4. Executa a função `execute_from_command_line` passando os argumentos da linha de comando 
   (`sys.argv`), permitindo que o usuário invoque comandos do Django via terminal.

Funções:
--------
- main(): Configura as variáveis de ambiente necessárias e executa os comandos administrativos 
  do Django.

Exemplo de Uso:
---------------
Para executar comandos administrativos em um projeto Django, rode o script no terminal:
    $ python manage.py runserver
    $ python manage.py migrate

Este script geralmente é chamado como `manage.py` na raiz de um projeto Django, mas pode ser 
adaptado conforme necessário.

Nota:
-----
Certifique-se de que o Django está instalado e que você está rodando o script dentro de um ambiente 
virtual adequado para evitar problemas de importação.
"""

import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            """Não foi possível importar o Django. Você tem certeza de que ele está
            instalado e disponível na variável de ambiente PYTHONPATH? Você 
            esqueceu de ativar um ambiente virtual?"""
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
