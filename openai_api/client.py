"""
Este módulo utiliza a API da OpenAI para gerar descrições de venda de carros.

Includes:
    - get_car_ai_bio: Gera uma descrição persuasiva e informativa de um carro com base no modelo, marca e ano.
"""

import openai
import os
from dotenv import load_dotenv


def get_car_ai_bio(model, brand, year):
    """
    Gera uma descrição de venda para um carro usando a API da OpenAI.

    Args:
        model (str): O modelo do carro.
        brand (str): A marca do carro.
        year (int): O ano de fabricação do carro.

    Returns:
        str: Uma descrição de venda do carro gerada pela OpenAI.
    """
    prompt = f"""Me mostre uma descrição de venda para o carro {brand} {model} {year} em 
        apenas 250 caracteres. Fale coisas específicas desse modelo de carro. 
        Descreva especificações técnicas desse modelo de carro de uma forma que 
        convença o consumidor a comprar o carro. Além disso, informe se o carro consome gasolina ou álcool.
        Adicione também se ele é um carro que pode ser abastecido com álcool e gasolina ou apenas uma das duas opções."""

    load_dotenv()
    OPENAI_API_KEY = os.getenv("API_KEY")
    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=1000
    )

    return response["choices"][0]["text"]
