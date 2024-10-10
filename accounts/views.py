"""
Este módulo fornece views para registro, login e logout de usuários utilizando Django.

Views:
    - register_view: Exibe o formulário de registro e cria um novo usuário se o formulário for válido.
    - login_view: Exibe o formulário de login e autentica o usuário se as credenciais forem válidas.
    - logout_view: Faz o logout do usuário atual e redireciona para a lista de carros.

Dependências:
    - django.contrib.auth.forms.UserCreationForm: Formulário de criação de novos usuários.
    - django.contrib.auth.forms.AuthenticationForm: Formulário de autenticação de usuários existentes.
    - django.contrib.auth.authenticate: Função para autenticar um usuário com base em credenciais.
    - django.contrib.auth.login: Função para logar um usuário autenticado.
    - django.contrib.auth.logout: Função para deslogar o usuário atual.
    - django.shortcuts.render: Renderiza um template com um contexto.
    - django.shortcuts.redirect: Redireciona para outra URL.
    - django.contrib.messages: Módulo para adicionar mensagens às respostas.

Cada view trata uma funcionalidade específica para a autenticação de usuários e utiliza 
os respectivos formulários e funções do Django para processar as requisições.
"""

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def register_view(request):
    """
    Exibe um formulário de registro e cria um novo usuário se o formulário for válido.

    Redireciona para a página de login após o sucesso.

    Args:
        request (HttpRequest): O objeto de requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP com a página de registro ou um redirecionamento para a
        página de login.
    """
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("cars_list")
    else:
        user_form = UserCreationForm()
    return render(request, "register.html", {"user_form": user_form})


def login_view(request):
    """
    Exibe um formulário de login e autentica o usuário se as credenciais forem válidas.

    Redireciona para a lista de carros após o sucesso.

    Args:
        request (HttpRequest): O objeto de requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP com a página de login ou um redirecionamento para a lista
        de carros.
    """
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("cars_list")
        else:
            messages.error(request, "Usuário ou senha inválidos.")

        login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, "login.html", {"login_form": login_form})


def logout_view(request):
    """
    Faz o logout do usuário atual e redireciona para a lista de carros.

    Args:
        request (HttpRequest): O objeto de requisição HTTP.

    Returns:
        HttpResponse: Um redirecionamento para a lista de carros.
    """
    logout(request)
    return redirect("cars_list")
