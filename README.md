
# Django Master Carros 🚗

Um sistema de gerenciamento de carros desenvolvido com Django, HTML, CSS e JavaScript. O projeto permite adicionar, editar, visualizar e excluir carros de um inventário, além de gerenciar contas de usuário.

## Tecnologias Utilizadas 🛠️

- **Django**: Framework principal para o desenvolvimento backend.
- **Python**: Linguagem de programação usada no projeto.
- **HTML/CSS**: Para estruturação e estilização das páginas.
- **JavaScript**: Para interatividade nas páginas.
- **SQLite**: Banco de dados utilizado para armazenamento de dados durante o desenvolvimento.
- **OpenAI API**: Utilizada para gerar descrições de carros com base no modelo, marca e ano.

## Estrutura do Projeto 📂

A estrutura do projeto está organizada da seguinte forma:

```
Django-Master-Carros/
├── accounts/
│   ├── static/accounts/
│   │   └── styles.css
│   ├── templates/
│   │   ├── login.html
│   │   └── register.html
│   ├── __init__.py
│   ├── apps.py
│   └── views.py
├── app/
│   ├── static/app/
│   │   ├── script/
│   │   │   └── theme_toggle.js
│   │   └── styles/
│   │       ├── base.css
│   │       ├── cars.css
│   │       ├── cars_delete.css
│   │       ├── cars_detail.css
│   │       ├── cars_update.css
│   │       └── new_car.css
│   ├── templates/
│   │   └── base.html
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── cars/
│   ├── migrations/
│   ├── templates/
│   │   ├── car_delete.html
│   │   ├── car_detail.html
│   │   ├── car_update.html
│   │   ├── cars.html
│   │   └── new_car.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   └── views.py
├── docs/
├── media/
├── openai_api/
├── venv/
├── .gitignore
├── carros_uwsgi.ini
├── db.sqlite3
├── manage.py
└── requirements.txt
```

### Principais Pastas e Arquivos

- **accounts/**: Módulo responsável pelo gerenciamento de contas de usuário, contendo as views e templates para login e registro.
- **cars/**: Módulo principal para gerenciamento de carros, com os templates, views, formulários e modelos relacionados.
- **openai_api/**: Implementação da integração com a API da OpenAI para geração de descrições.
- **static/**: Arquivos estáticos, como estilos CSS e scripts JavaScript.
- **templates/**: Diretório de templates HTML.
- **venv/**: Ambiente virtual com dependências do projeto.
- **requirements.txt**: Arquivo com as dependências necessárias para rodar o projeto.

## Funcionalidades 🚀

- Registro, login e logout de usuários.
- CRUD (Create, Read, Update, Delete) completo para gerenciamento de carros.
- Geração automática de descrições de carros usando a API da OpenAI.
- Interface amigável com templates customizados em HTML e CSS.

## Como Executar o Projeto 🔧

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/Django-Master-Carros.git
   ```
2. **Entre no diretório do projeto:**
   ```bash
   cd Django-Master-Carros
   ```
3. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows
   venv\Scripts\activate
   # No Unix ou MacOS
   source venv/bin/activate
   ```
4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Realize as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```
6. **Execute o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```
7. **Acesse o projeto no navegador:**
   Abra o navegador e acesse `http://127.0.0.1:8000/`.

## Configuração da API OpenAI 🌐

Para utilizar a funcionalidade de geração de descrições, você precisará configurar a chave da API da OpenAI:

1. Crie um arquivo `.env` na raiz do projeto.
2. Adicione sua chave de API no formato:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Contribuindo 🤝

Contribuições são bem-vindas! Se você tiver sugestões ou encontrar problemas, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.
