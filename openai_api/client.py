"""
Car AI Description Generator

Este módulo utiliza a API da OpenAI para gerar descrições de venda persuasivas para carros,
baseadas no modelo, marca e ano fornecidos. As descrições são limitadas a 250 caracteres e incluem
especificações técnicas e informações de abastecimento.

Dependências:
-------------
- openai: Biblioteca para acessar a API da OpenAI.
- os: Biblioteca padrão para acessar variáveis de ambiente.
- dotenv: Biblioteca para carregar variáveis de ambiente de um arquivo .env.
"""

import openai
import os
from dotenv import load_dotenv


def get_car_ai_bio(model, brand, year):
    """
    Gera uma descrição de venda para um carro específico usando a API da OpenAI.

    Cria um prompt pedindo uma descrição breve e persuasiva do carro, incluindo
    especificações técnicas e opções de combustível. Carrega as variáveis de ambiente
    e utiliza a chave da API da OpenAI para gerar a descrição.

    Parâmetros:
        model (str): O modelo do carro.
        brand (str): A marca do carro.
        year (int): O ano do carro.

    Retorna:
        str: Texto gerado pela API da OpenAI como descrição do carro.

    Configuração:
        Certifique-se de que o arquivo `.env` contenha a variável `API_KEY` com
        a chave correta da API OpenAI.
    """
    prompt = (
        f"Me mostre uma descrição de venda para o carro {brand} {model} {year} em "
        "apenas 250 caracteres. Fale coisas específicas desse modelo de carro. "
        "Descreva especificações técnicas desse modelo de carro de uma forma que "
        "convença o consumidor a comprar o carro. Além disso, informe se o carro consome "
        "gasolina ou álcool. Adicione também se ele é um carro que pode ser abastecido "
        "com álcool e gasolina ou apenas uma das duas opções."
    )

    load_dotenv()
    OPENAI_API_KEY = os.getenv("API_KEY")
    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=1000
    )

    return response["choices"][0]["text"]
