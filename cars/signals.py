"""
Car Signals Module

Este módulo contém os manipuladores (handlers) para os sinais `post_save`, `post_delete`, e `pre_save` 
do modelo `Car`. Ele é responsável por manter o inventário de carros atualizado e gerar automaticamente 
uma biografia para um carro antes de ser salvo no banco de dados.

Dependências:
-------------
- django.db.models.signals: Sinais utilizados para capturar os eventos de criação, atualização e deleção no modelo.
- django.db.models: Utilizado para calcular o total e o valor agregado de carros.
- django.dispatch.receiver: Decorador usado para associar funções aos sinais.
- cars.models.Car: O modelo de dados para carros.
- cars.models.CarInventory: Modelo de dados para manter o inventário de carros.
- openai_api.client.get_car_ai_bio: Função para gerar uma bio do carro utilizando a API da OpenAI.

Funções:
--------
- car_inventory_update(): Atualiza o inventário com a quantidade total de carros e o valor agregado.
- car_pre_save(sender, instance, **kwargs): Gera automaticamente uma biografia do carro usando a API da OpenAI antes de salvá-lo.
- car_post_save(sender, instance, **kwargs): Executa o processo de atualização do inventário após um carro ser salvo.
- car_post_delete(sender, instance, **kwargs): Atualiza o inventário após um carro ser deletado.

Fluxo de Execução:
------------------
1. **car_pre_save**: Antes de salvar o carro, verifica se ele tem uma bio. Caso não tenha, gera uma descrição automática.
2. **car_post_save**: Após salvar um carro (novo ou editado), a função atualiza o inventário de carros no sistema.
3. **car_post_delete**: Após a deleção de um carro, o inventário é atualizado para refletir a remoção.
4. **car_inventory_update**: Função auxiliar que recalcula o número total de carros e o valor agregado dos veículos para manter o inventário atualizado.

Exemplo de Uso:
---------------
Este módulo é carregado automaticamente com o aplicativo Django. Ele escuta eventos de criação, edição e exclusão no modelo `Car`, 
mantendo o inventário atualizado sem necessidade de intervenção manual.
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
