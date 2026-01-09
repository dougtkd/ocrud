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

def make_response(msg: str, args: dict = {}):
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
    - ler os dados enviados JSON
    - verifica se os dados são válidos
    - criar o produto
    - enviar o produto pra camada de serviço
    - retorna o resultado para o usuário
    """
    try:
        # TODO
        payload = request.json

        if not payload:
            raise ValueError("JSON inválido!")

        produto = ProductModel(
            id=None,
            name=payload.get("name"),
            price=payload.get("price"),
            stock=payload.get("stock", 0)
        )
       
        prod_id = service.insert(produto)

        logging.debug(f"[PRODUCT-API] Product created with ID={prod_id}")

        return make_response(
            "Product created",
            {"id": prod_id}
        ), HTTPStatus.CREATED
       
    except Exception as error: 
        # a exceção que vai ser retornada se der algum B.O. durante o processamento
        errorMsg = f"Error to try process request: Invalid request {error}"
        logging.error(f"[PRODUCT-API] {errorMsg}")
        return make_response(errorMsg), HTTPStatus.BAD_REQUEST

@app.route("/products", methods = ['GET'])
def get():
    """
    Rota responsável por listar os produtos cadastrados!
    
    Essa rota não está recebendo parâmetros, para apenas retornar a lista completa dos produtos!
    """
    
    try:
        # TODO
        produtos = service.get()

        return make_response(
            "All products", {"payload": [p.toDict() for p in produtos]}
        ), HTTPStatus.OK
                
    except Exception as error: 
        # Essa exceção pega todo erro inesperado enquanto processa!
        errorMsg = f"Error to try get all products: {error}"
        logging.error(f"[PRODUCT-API] {errorMsg}")
        return make_response(errorMsg), HTTPStatus.INTERNAL_SERVER_ERROR    

@app.route("/products/<id>", methods = ['GET'])
def getById(id):
    """
    Rota que busca um produto específico pelo seu ID!

    O ID do produto vem pela URL da rota (PATH).
    """
    
    try:
        # TODO:
        produto = service.getById(int(id))

        if not produto:
            return make_response("Produto não encontrado!"), HTTPStatus.NOT_FOUND

        return make_response(f"Product id {id}", {"payload": produto.toDict()}), HTTPStatus.OK
        
    except Exception as error: 
        errorMsg = f"Error to try get product id {id}: {error}"
        logging.error(f"[PRODUCT-API] {errorMsg}")
        return make_response(errorMsg), HTTPStatus.INTERNAL_SERVER_ERROR

# TODO UPDATE
@app.route("/products/<id>", methods=['PUT'])
def update(id):
    """
    Rota que atualiza um produto 

    
    """
    try:
        payload = request.json

        produto = ProductModel(
            id=int(id),
            name=payload.get("name"),
            price=payload.get("price"),
            stock=payload.get("stock")
        )

        atualiza = service.update(produto)

        if not atualiza:
            return make_response("Produto não encontrado!"), HTTPStatus.NOT_FOUND

        return make_response("Produto atualizado!"), HTTPStatus.OK

    except Exception as error:
        logging.error(f"[PRODUCT-API] {error}")
        return make_response(str(error)), HTTPStatus.BAD_REQUEST
    
# TODO DELETE   
@app.route("/products/<id>", methods=['DELETE'])
def delete(id):
    """
    Rota que deleta um produto

    
    """
    try:
        remove = service.delete(int(id))

        if not remove:
            return make_response("Produto não encontrado!"), HTTPStatus.NOT_FOUND

        return make_response("Produto deletado!"), HTTPStatus.OK

    except Exception as error:
        logging.error(f"[PRODUCT-API] {error}")
        return make_response(str(error)), HTTPStatus.BAD_REQUEST

if __name__ == "__main__":
    print("App Ready and Running!")
    app.run(debug=True, host='0.0.0.0', port=5000)
