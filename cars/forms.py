"""
Car Model Form Module

Este módulo define um formulário para o modelo Car, incluindo validações personalizadas
para garantir a integridade dos dados ao criar ou atualizar instâncias de Car.

Dependências:
-------------
- django.forms: Biblioteca do Django para criar formulários baseados em modelos.
- cars.models.Car: O modelo de dados para carros utilizado no formulário.
"""

from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    """
    Um formulário para o modelo Car, incluindo validações personalizadas.
    """

    class Meta:
        model = Car
        fields = "__all__"

    def clean_value(self):
        """
        Valida o campo 'value' do formulário. Garante que o valor seja pelo menos R$20.000.

        Returns:
            float: O valor do carro se a validação for bem-sucedida.

        Raises:
            ValidationError: Se o valor for menor que R$20.000.
        """
        value = self.cleaned_data.get("value")
        if value < 20000:
            self.add_error("value", "Valor mínimo do carro deve ser de R$20.000!")
        return value

    def clean_factory_year(self):
        """
        Valida o campo 'factory_year' do formulário. Garante que o ano de fabricação seja superior a 1985.

        Returns:
            int: O ano de fabricação do carro se a validação for bem-sucedida.

        Raises:
            ValidationError: Se o ano de fabricação for menor que 1985.
        """
        factory_year = self.cleaned_data.get("factory_year")
        if factory_year < 1985:
            self.add_error(
                "factory_year",
                "A fabricação do carro deve ser superior ao ano de 1985!",
            )
        return factory_year
