"""
Configuração WSGI para o projeto Django.

Descrição:
----------
Este script configura o ambiente WSGI para o projeto Django e fornece
o objeto `application` para ser usado pelo servidor WSGI.

Configurações:
--------------
- Variável de ambiente `DJANGO_SETTINGS_MODULE` configurada para `app.settings`.

Função:
-------
- `get_wsgi_application()`: Retorna um objeto WSGI aplicável para servir o Django.

Autores:
--------
- Desenvolvido com o framework Django.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
application = get_wsgi_application()
