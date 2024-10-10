"""
Módulo de views para o aplicativo 'cars'.

Este módulo fornece views genéricas para operações de CRUD (Create, Read, Update, Delete) sobre o modelo Car.
As views permitem listar, criar, detalhar, atualizar e deletar carros no sistema. Algumas views requerem
autenticação do usuário para acesso.

Classes:
    - CarsListView: View para listar os carros disponíveis.
    - CarDetailView: View para exibir detalhes de um carro específico.
    - NewCarCreateView: View para criar um novo carro (requer autenticação).
    - CarUpdateView: View para atualizar um carro existente (requer autenticação).
    - CarDeleteView: View para deletar um carro existente (requer autenticação).

Dependências:
    - cars.models.Car: Modelo de dados usado pela aplicação.
    - cars.forms.CarModelForm: Formulário usado para criar e atualizar um carro.
    - django.contrib.auth.decorators.login_required: Decorador para exigir autenticação do usuário.
    - django.utils.decorators.method_decorator: Decorador de funções para métodos de classe.
    - django.urls.reverse_lazy: Utilitário para construir URLs por meio de nomes de view.
    - django.views.generic.*: Views genéricas do Django para operações CRUD.
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
    View para listar os carros disponíveis.

    Lista os carros cadastrados no sistema, permitindo a busca filtrada por modelo, ano de fabricação e marca.
    O resultado é ordenado por modelo.

    Atributos:
        model (Model): O modelo de carro utilizado.
        template_name (str): O template usado para renderizar a lista de carros.
        context_object_name (str): O nome do contexto definido para acessar os objetos no template.

    Métodos:
        get_queryset(self): Retorna o queryset filtrado de carros baseado nos parâmetros de busca.
        get_context_data(self, **kwargs): Adiciona anos e marcas ao contexto para populações de dropdown.
    """

    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        """
        Obtém o conjunto de objetos Car, aplicando filtros baseados em busca de modelo, anode fabricação, ano do modelo e marca.

        Retorna:
            QuerySet: Lista de carros filtrada e ordenada por modelo.
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

        Inclui listas distintas de anos e todas as marcas disponíveis para populações de dropdown.

        Retorna:
            dict: Contexto atualizado com anos e marcas.
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
    View para exibir os detalhes de um carro específico.

    Exibe informações detalhadas sobre um carro selecionado.

    Atributos:
        model (Model): O modelo de dados usado pela view.
        template_name (str): O nome do template usado para renderizar a view.
        context_object_name (str): O nome do objeto no contexto do template.
    """

    model = Car
    template_name = "car_detail.html"
    context_object_name = "car"


@method_decorator(login_required(login_url="login"), name="dispatch")
class NewCarCreateView(CreateView):
    """
    View para criar um novo carro.

    Esta view exibe um formulário para a criação de um novo carro e redireciona para a lista de carros após a criação bem-sucedida.
    É necessário que o usuário esteja autenticado para acessar a view, sendo redirecionado para a página de login se não estiver autenticado.

    Attributes:
        model (Model): O modelo de dados usado pela view.
        form_class (Form): O formulário usado para criar um novo carro.
        template_name (str): O nome do template usado para renderizar a view.
        success_url (str): A URL para a qual redirecionar após a criação bem-sucedida.
    """

    model = Car
    form_class = CarModelForm
    template_name = "new_car.html"
    success_url = "/cars/"


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarUpdateView(UpdateView):
    """
    View para atualizar um carro existente.

    Exibe um formulário para a atualização de um carro e redireciona para os detalhes do carro após o sucesso.
    É necessário que o usuário esteja autenticado para acessar a view, sendo redirecionado para a página de login se não estiver autenticado.

    Atributos:
        model (Model): O modelo de dados usado pela view.
        form_class (Form): O formulário usado para atualizar o carro.
        template_name (str): O nome do template usado para renderizar a view.
    """

    model = Car
    form_class = CarModelForm
    template_name = "car_update.html"

    def get_success_url(self):
        """
        Retorna a URL de sucesso após a atualização bem-sucedida.

        Returns:
            str: A URL para os detalhes do carro atualizado.
        """
        return reverse_lazy("car_detail", kwargs={"pk": self.object.pk})


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarDeleteView(DeleteView):
    """
    View para deletar um carro existente.

    Exibe um formulário de confirmação para deletar um carro e redireciona para a lista de carros após a exclusão.
    É necessário que o usuário esteja autenticado para acessar a view, sendo redirecionado para a página de login se não estiver autenticado.

    Atributos:
        model (Model): O modelo de dados usado pela view.
        template_name (str): O nome do template usado para renderizar a view.
        success_url (str): A URL para a qual redirecionar após a exclusão bem-sucedida.
    """

    model = Car
    template_name = "car_delete.html"
    success_url = "/cars/"
