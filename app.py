#!/bin/env python3
"""
Flask - framework que vamos usar pro código ficar funcional através das rotas http (endpoints)

Missão: 
- Receber e validar as requisições
- Fazer as regras de negócio funcionarem na camada de serviço
- Ser forte e corajoso

OBS: 
- Vi em um vídeo que de forma alguma posso colocar a regra de negócio aqui
- Funciona puxando direto do banco de dados
"""

import logging
from flask import Flask, request, jsonify
from http import HTTPStatus
from datetime import datetime
import json 

# Importação das camadas do programa
from models.product import ProductModel
from services.product import ProductService

# Só um aviso pro usuário que o programa está começando a rodar
print("Starting...")

# O Flask recebe o __name__ pra achar tudo o que o app precisa pra rodar (acho)
app = Flask(__name__)

# Aqui tudo que for relacionado a service vai ser responsabilidade do objeto ProductService()
service = ProductService()

# Aqui vão ficar as configurações dos logging do programa
logging.basicConfig(
    level=logging.DEBUG, # Debuga!
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="logs/products-service.log", # Retorna o arquivo do log
    filemode='a', # um Append, adiciona o log em algum lugar 
    datefmt='%H:%M:%S',
)

# Avisa pro usuário que o programa carregou e está pronto
print("Exiting...")

def makeResponse(msg: str, args: dict = {}):
"""
Essa função cria uma resposta padrão para API!

- message: de fato uma mensagem
- timestamp: retorna a data e a hora da resposta

parametro msg recebe string 
parametro arg recebe um dicionário vazio

"""

    # Resposta
    ret = {
        "message": msg,
        "timestamp": datetime.now().isoformat()
    }

    # Adiciona dados extras
    for key in args:
        ret[key] = args[key]

    return ret

@app.route("/products", methods = ['POST'])
def insert():
    """
    Rota responsável por cadastrar novo produto.

    Fluxo:
    - ler os dados enviados JSON
    - verifica se os dados são válidos
    - criar o produto
    - enviar o produto pra camada de serviço
    - retorna o resultado para o usuário
    """
    try:
        # Armazena o ID gerado pelo banco!
        id = ""
        # TODO
        # - fazer ler o request.json
        # - validar nome e preço
        # - criar ProductModel
        # - chamar o service.insert do produto

        # log para verificar o que chegou na requisição
        logging.debug(f"[PRODUCT-API] Request data: {request.data}")

        # se não implementar, retorna o not_implemented
        return makeResponse(f"All products"), HTTPStatus.NOT_IMPLEMENTED
        
    except Exception as error: 
        # a exceção que vai ser retornada se der algum B.O. durante o processamento
        errorMsg = f"Error to try process request: Invalid request {error}"
        logging.error(f"[PRODUCT-API] {errorMsg}")
        return makeResponse(errorMsg), HTTPStatus.BAD_REQUEST

@app.route("/products", methods = ['GET'])
def get():
    """
    Rota responsável por listar os produtos cadastrados!
    
    Essa rota não está recebendo parâmetros, para apenas retornar a lista completa dos produtos!
    """
    
    ret = {} # Variável ainda não necessária na rota! Mas o intuito dela é armazenar o retorno do serviço.
    
    try:
        # TODO
        # - Acho que temos que chamar o método service.get() aqui
        # - converter produtos para dict/json
        # - Retornar a lista de produtos
        
        return makeResponse(f"All products"), HTTPStatus.NOT_IMPLEMENTED
    except Exception as error: 
        # Essa exceção pega todo erro inesperado enquanto processa!
        errorMsg = f"Error to try get all products: {error}"
        logging.error(f"[PRODUCT-API] {errorMsg}")
        return makeResponse(errorMsg), HTTPStatus.INTERNAL_SERVER_ERROR    

@app.route("/products/<id>", methods = ['GET'])
def getById(id):
    """
    Rota que busca um produto específico pelo seu ID!

    O ID do produto vem pela URL da rota (PATH).
    """
    # variável que vai salvar o produto encontrado.
    ret = {}
    try:
        # TODO:
        # - Acho que devemos validar o ID aqui
        # - chamar o service.getByID(id)
        # - retornar o produto encontrado

        # ret.toDict só vai significar algo uando ret for um objeto ProductModel!
        return makeResponse(f"Product id {id}", { "data": ret.toDict() }), HTTPStatus.NOT_IMPLEMENTED
    except Exception as error: 
        errorMsg = f"Error to try get product id {id}: {error}"
        logging.error(f"[PRODUCT-API] {errorMsg}")
        return makeResponse(errorMsg), HTTPStatus.INTERNAL_SERVER_ERROR    

# TODO UPDATE
    # - Rota para atualizar um produto
    # - URL PUT /products/id
    # - Receber dados
    # - Atualizar o produto já existente
    
# TODO DELETE   
    # - Rota para remover um produto
    # - URL DELETE /products/id
    # - excluir produto do banco 
