"""
Vistas de autenticação para um projeto Django.

Descrição:
----------
Este módulo fornece vistas para registro, login e logout de usuários.

Importações:
------------
- Formulários e funções de autenticação do Django.
- Funções de gerenciamento de sessões e mensagens.
- Utilidades para renderização de templates e redirecionamentos.

Funções:
--------
- register_view: Lida com a criação de novos usuários.
- login_view: Gerencia o processo de login de usuários existentes.
- logout_view: Faz logout do usuário atual e redireciona para a página de listagem de carros.

Notas:
------
- Mensagens de erro são exibidas para informar o usuário sobre falhas na autenticação.

Autores:
--------
- Desenvolvido com base no framework Django.
"""

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def register_view(request):
    # Gerencia o registro de novos usuários.
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("cars_list")
    else:
        user_form = UserCreationForm()
    return render(request, "register.html", {"user_form": user_form})


def login_view(request):
    # Lida com o processo de login.
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
    # Faz logout do usuário e redireciona.
    logout(request)
    return redirect("cars_list")
