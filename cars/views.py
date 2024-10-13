"""
Car CRUD Views Module

Este módulo contém as views para as operações de CRUD (Create, Read, Update, Delete) do modelo `Car`
no aplicativo 'cars'. As views permitem listar, visualizar detalhes, criar, atualizar e excluir
carros. Algumas dessas operações exigem que o usuário esteja autenticado.

Dependências:
-------------
- cars.models.Car: Modelo de dados do carro.
- cars.models.Brand: Modelo relacionado à marca dos carros.
- cars.forms.CarModelForm: Formulário usado para criação e atualização dos carros.
- django.contrib.auth.decorators.login_required: Decorador que garante que o usuário esteja autenticado para acessar certas views.
- django.utils.decorators.method_decorator: Decorador para métodos de classe.
- django.urls.reverse_lazy: Utilitário para gerar URLs de maneira preguiçosa (lazy).
- django.views.generic: Views genéricas do Django utilizadas para manipulação CRUD.
"""

from cars.models import Car, Brand
from cars.forms import CarModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)


class CarsListView(ListView):
    """
    View para listar os carros cadastrados no sistema.

    Atributos:
        model (Model): O modelo do carro.
        template_name (str): Template usado para a lista de carros.
        context_object_name (str): Nome no contexto do template para acessar os carros.
    """

    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        """
        Retorna um queryset filtrado de carros.

        Filtra a lista de carros baseado em parâmetros de busca como modelo, ano de fabricação,
        ano do modelo e marca, ordenando por modelo.

        Retorna:
            QuerySet: Carros filtrados e ordenados.
        """
        cars = super().get_queryset().order_by("model")
        search = self.request.GET.get("search")
        year = self.request.GET.get("year")
        model_year = self.request.GET.get("model_year")
        brand = self.request.GET.get("brand")

        if search:
            cars = cars.filter(model__icontains=search)
        if year:
            cars = cars.filter(factory_year__icontains=year)
        if brand:
            cars = cars.filter(brand__name__icontains=brand)
        if model_year:
            cars = cars.filter(model_year=model_year)

        return cars

    def get_context_data(self, **kwargs):
        """
        Adiciona dados adicionais ao contexto do template.

        Inclui listas de anos e marcas disponíveis para facilitar a filtragem.

        Retorna:
            dict: O contexto atualizado com informação adicional.
        """
        context = super().get_context_data(**kwargs)
        context["years"] = Car.objects.values_list("factory_year", flat=True).distinct()
        context["model_years"] = Car.objects.values_list(
            "model_year", flat=True
        ).distinct()
        context["brands"] = Brand.objects.all()
        return context


class CarDetailView(DetailView):
    """
    View para exibir detalhes de um carro específico.

    Atributos:
        model (Model): O modelo de dados do carro.
        template_name (str): Template usado para renderizar detalhes do carro.
        context_object_name (str): Nome do carro no contexto do template.
    """

    model = Car
    template_name = "car_detail.html"
    context_object_name = "car"


@method_decorator(login_required(login_url="login"), name="dispatch")
class NewCarCreateView(CreateView):
    """
    View para criar um novo carro.

    Requer que o usuário esteja autenticado.

    Atributos:
        model (Model): Modelo de dados para o carro.
        form_class (Form): Formulário para criação de novos carros.
        template_name (str): Template usado para o formulário de criação.
        success_url (str): URL de redirecionamento após a criação.
    """

    model = Car
    form_class = CarModelForm
    template_name = "new_car.html"
    success_url = "/cars/"


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarUpdateView(UpdateView):
    """
    View para atualizar um carro existente.

    Requer que o usuário esteja autenticado.

    Atributos:
        model (Model): Modelo de dados para o carro.
        form_class (Form): Formulário para atualização de carros.
        template_name (str): Template usado para o formulário de atualização.
    """

    model = Car
    form_class = CarModelForm
    template_name = "car_update.html"

    def get_success_url(self):
        """
        Define a URL de sucesso após a atualização.

        Retorna:
            str: URL para os detalhes do carro atualizado.
        """
        return reverse_lazy("car_detail", kwargs={"pk": self.object.pk})


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarDeleteView(DeleteView):
    """
    View para deletar um carro existente.

    Requer que o usuário esteja autenticado.

    Atributos:
        model (Model): Modelo de dados para o carro.
        template_name (str): Template usado para confirmação de exclusão.
        success_url (str): URL de redirecionamento após exclusão.
    """

    model = Car
    template_name = "car_delete.html"
    success_url = "/cars/"
