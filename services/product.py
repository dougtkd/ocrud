import logging # importa biblioteca padrão para registrar logs
import traceback # importa para salvar o erro completo, entender em qual linha e qual chamada o erro aconteceu

# camada que acessa o banco de dados
from storage.product import ProductStorage # responsável por conversar diretamente com o banco. OBS: o service não lê SQL, só chama métodos do Storage

# modelo do produto no nosso sistema
from models.product import ProductModel # representa o produto dentro do sistema
# O service trabalha com modelos, nunca com dicts soltos

class ProductService:
    """
    Essa classe é a camada de serviço!
    - É aqui que vão ficar as regras de negócio
    - Validaremos os dados antes de salvar ou consultar
    - Faz o meio de campo entre o app.py e o storage (API e banco)

    Aparetemente a API não acessa o banco diretamente, então é papel do service ajudar nessa parte já que o banco não conhece regras de negócio!
    """
    
    def __init__(self):
        """
        Constructor do serviço de produto
        - Aqui é criado a instância do storage que será usada para acessar os dados do banco.
        """
        self.storage = ProductStorage() # cria uma instância da classe ProductStorage e salva na variável self.storage

    def insert(self, prod:ProductModel) -> int: # método recebe o objeto ProductModel e devolve um inteiro (id)
        """
        Método que insere novo produto no sistema!
        -recebe o ProductModel do app.py
        -valida e aplica as regras
        -Pede para o storage que salve nosso produto
        -Deve retornar o id do produto salvo
        """
        try:
            # TODO
            if not prod.name: # verificação se o nome do prod está vazio
                raise ValueError("Nome do produto obrigatório!") # se estiver, para e retorna erro

            if prod.price < 0: # verificação se o preço é negativo
                raise ValueError("Preço inválido!") # se for, para e retorna erro

            if prod.stock < 0: #verificação se o estoque é negativo
                raise ValueError("Estoque inválido!") # se for, para e retorna erro

            prod_id = self.storage.insert(prod) # salva o objeto prod no banco pelo método insert
            
            logging.debug(f"[PRODUCT-SERVICE] Insert Product: {prod.toJson()}") # converte os dados do produto para o formato JSON
            return prod_id # retorna o id 
            
        except Exception as error:
            # Exceção que pega todo erro ocorrido no processo
            # esse traceback.format_exc ajuda entender onde esse possível erro aconteceu, mapeia o erro
            logging.error(f"[PRODUCT-SERVICE] Fail: {error} -> {traceback.format_exc()}") 
            raise error # se achar, para e retorna error
            
    def get(self) -> list:
        """
        Método que retorna todos os produtos cadastrados!
        - pede para o storage a lista de produtos
        - e retorna essa lista para o app.py
        """
        
        try:
            # TODO
            produtos = self.storage.get() # service chama o método get do storage e salva na variável produtos
            logging.debug(f"[PRODUCT-SERVICE] Get all Products: {len(produtos)} found") # monitora e conta quantos itens foram retornados
            return produtos # retorna a lista de produtos
        
        except Exception as error: 
            logging.error(f"[PRODUCT-SERVICE] Fail: {error} -> {traceback.format_exc()}") # mapeia erro
            raise error # se achar, para e retorna o erro

    def getById(self, id:int) -> ProductModel:
        """
        Método que retorna um produto pelo id dele!
        1. recebe o id solicitado pelo app.py
        2. pede pro storage o produto que corresponde o id
        3. retorna Product Model
        """
        
        try:
            # TODO
            if id <= 0: # verifica se o id é zero ou negativo
                raise ValueError("ID inválido!") # se sim, para e retorna erro

            produto = self.storage.getById(id) # pede pro storage buscar no banco um registro através do id e salva na variável produto
            
            logging.debug(f"[PRODUCT-SERVICE] Get Product by ID: {id}") 
            return produto # retorna o objeto encontrado
            
        except Exception as error: 
            logging.error(f"[PRODUCT-SERVICE] Fail: {error} -> {traceback.format_exc()}") # mapeia o erro
            raise error # se achar, para e retorna o error
    
    # TODO UPDATE
    def update(self, prod: ProductModel) -> bool:
        """
        Método que atualiza produto
        -recebe um Product Model
        -valida se o produto tem id
        -chama o storage para atualizar
        -retorna true ou false
        """
        
        try:
            if not prod.id: # verifica se o objeto prod tem id
                raise ValueError("Produto sem ID!") # se não tiver, para! e retorna error

            return self.storage.update(prod) # retorna true se atualizou, false se o id não foi encontrado

        except Exception as error:
            logging.error(f"[PRODUCT-SERVICE] Fail: {error} -> {traceback.format_exc()}") # mapeia o erro
            raise error # se achar, para e retorna error
            
    # TODO DELETE
    def delete(self, id: int) -> bool:
        """
        Método que remove um produto do banco
        -recebe o id
        -valida esse id
        -chama o storage pra deletar
        -retorna true ou false
        """
        
        try:
            if id <= 0: # verifica se o id é zero ou negativo
                raise ValueError("ID inválido!") # se for, para e retorna erro

            return self.storage.delete(id) # retorna true se o produto foi removido, false se o id não existe

        except Exception as error:
            logging.error(f"[PRODUCT-SERVICE] Fail: {error} -> {traceback.format_exc()}") # mapeia o erro
            raise error # se achar, para e retorna error
            
