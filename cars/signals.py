"""
Sinais da aplicação 'cars'.

Este módulo define handlers para os sinais post_save e post_delete do modelo Car.

Funções:
   car_inventory_update(): Atualiza o inventário de carros.
   car_pre_save(sender, instance, **kwargs): Gera uma bio para o carro antes de salvar.
   car_post_save(sender, instance, **kwargs): Handler para o sinal post_save do modelo Car.
   car_post_delete(sender, instance, **kwargs): Handler para o sinal post_delete do modelo Car.
"""

from django.db.models.signals import post_save, post_delete, pre_save
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from openai_api.client import get_car_ai_bio


def car_inventory_update():
    """
    Atualiza o inventário de carros.

    Calcula o total de carros e o valor agregado de todos os carros,
    e cria uma nova entrada em CarInventory com esses valores.
    """
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(total_value=Sum("value"))["total_value"]
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    """
    Gera uma bio para o carro antes de salvar.

    Se a instância de Car não possui bio, gera uma usando a API da OpenAI.

    Args:
        sender (Model): O modelo que enviou o sinal.
        instance (Car): A instância de Car que será salva.
        **kwargs: Argumentos adicionais.
    """
    if not instance.bio:
        ai_bio = get_car_ai_bio(instance.model, instance.brand, instance.model_year)
        instance.bio = ai_bio


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    """
    Handler para o sinal post_save do modelo Car.

    Executado depois de um objeto Car ser salvo.

    Args:
        sender (Model): O modelo que enviou o sinal.
        instance (Car): A instância de Car que foi salva.
        **kwargs: Argumentos adicionais.
    """
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    """
    Handler para o sinal post_delete do modelo Car.

    Executado depois de um objeto Car ser deletado.

    Args:
        sender (Model): O modelo que enviou o sinal.
        instance (Car): A instância de Car que foi deletada.
        **kwargs: Argumentos adicionais.
    """
    car_inventory_update()
