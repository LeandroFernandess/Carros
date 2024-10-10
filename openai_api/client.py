"""
Car Sales Description Generator

Este módulo utiliza a API da OpenAI para gerar descrições persuasivas e informativas de carros 
baseadas em seu modelo, marca e ano. A descrição gerada pode incluir informações técnicas e 
características específicas do veículo, com foco em convencer o consumidor.

Dependências:
-------------
- openai: Biblioteca necessária para interagir com a API da OpenAI.
- dotenv: Biblioteca utilizada para carregar variáveis de ambiente do arquivo `.env`, onde a chave de API 
  da OpenAI é armazenada de forma segura.
- API da OpenAI: A API da OpenAI é usada para gerar as descrições dos carros. A chave de API deve ser 
  definida no arquivo `.env` na variável `API_KEY`.

Instalação das dependências:
----------------------------
Você pode instalar as dependências necessárias utilizando `pip`:
    pip install openai python-dotenv

Variáveis de Ambiente:
----------------------
- API_KEY: Deve estar definida no arquivo `.env`, contendo a chave da API da OpenAI. O arquivo `.env` 
  será carregado automaticamente pelo módulo `dotenv` antes de fazer a chamada à API.

Fluxo de Execução:
------------------
1. O módulo começa carregando as variáveis de ambiente do arquivo `.env` através de `load_dotenv()`.
2. A chave da API da OpenAI (`API_KEY`) é recuperada do ambiente e usada para autenticação.
3. Um `prompt` detalhado é criado, incluindo o modelo, marca e ano do carro, solicitando uma descrição 
   de vendas focada em especificações técnicas e argumentos persuasivos.
4. O `prompt` é enviado à API da OpenAI, que retorna uma resposta com a descrição gerada.
5. O texto da resposta é extraído e retornado como a descrição do carro.

Funções:
--------
- get_car_ai_bio(model, brand, year): Gera uma descrição de venda persuasiva para um carro 
  com base nas informações fornecidas (modelo, marca e ano) utilizando a API da OpenAI.

Args:
-----
- model (str): O modelo do carro (ex: "Civic").
- brand (str): A marca do carro (ex: "Honda").
- year (int): O ano de fabricação do carro (ex: 2020).

Returns:
--------
- str: Uma descrição de venda do carro, incluindo detalhes técnicos e sugestões de combustível, 
  gerada pela API da OpenAI.

Exemplo de Uso:
---------------
Para gerar uma descrição de um carro específico:
    description = get_car_ai_bio("Civic", "Honda", 2020)
    print(description)

A descrição gerada conterá um texto persuasivo e informativo sobre o carro fornecido, 
incluindo especificações técnicas e detalhes sobre o consumo de combustível.
"""

import openai
import os
from dotenv import load_dotenv


def get_car_ai_bio(model, brand, year):

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
