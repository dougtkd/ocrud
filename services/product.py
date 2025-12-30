import logging
import traceback

# camada que acessa o banco de dados
from storage.product import ProductStorage

# modelo do produto no nosso sistema
from models.product import ProductModel

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
    - Aqui é criado a instância da camada do storage que será usada para acessar os dados do banco.
    """
        self.storage = ProductStorage()

    def insert(self, prod:ProductModel) -> int:
        """
        Método que insere novo produto no sistema!
        1. recebe o ProductModel do app.py
        2. valida e aplica as regras
        3. Pede para o storage que salve nosso produto
        4. Deve retornar o id do produto salvo
        """
        try:
            # TODO
            # - validar os dados do produto
            # - fazer o self.storage.insert
            # - receber o id dque o banco gerou do produto salvo
            # - retornar o id
            
            logging.debug(f"[PRODUCT-SERVICE] Insert Product: {prod.toJson()}")
        except Exception as error:
            # Exceção que pega todo erro ocorrido no processo
            # esse traceback.format_exc ajuda entender onde esse possível erro aconteceu, eu espero
            logging.error(f"[PRODUCT-SERVICE] Fail: {error} -> {traceback.format_exc()}")

        # essa variável só vai funcionar quando o to do acima foi feito!
        return id
            
    def get(self) -> list:
        """
        Método que retorna todos os produtos cadastrados!
        - pede para o storage a lista de produtos
        - e retorna essa lista para o app.py
        """
        # essa variável vai guardar os produtos retornados
        ret = {}
        
        try:
            # TODO
            # - chamar o self.storage.get
            # - guardar o retorno no ret
            
            logging.debug(f"[PRODUCT-SERVICE] Get all Products: {len(ret)} found")
        
        except Exception as error:
            logging.error(f"[PRODUCT-SERVICE] Fail: {error} -> {traceback.format_exc()}")
        
        return ret

    def getById(self, id:int) -> ProductModel:
        """
        Método que retorna um produto pelo id dele!
        1. recebe o id solicitado pelo app.py
        2. pede pro storage o produto que corresponde o id
        3. retorna produto
        """
        # essa variável vai guardar o produto retornado! 
        ret = {}
        
        try:
            # TODO
            # - ver se o id é de fato válido
            # - chama self.storage.getById
            # - guardar o produto no ret
            
            logging.debug(f"[PRODUCT-SERVICE] Get Product by ID: {id}")
        except Exception as error:
            logging.error(f"[PRODUCT-SERVICE] Fail: {error} -> {traceback.format_exc()}")

        return ret
    
    # TODO UPDATE
    # implementar todo o método de update
    # - atualizar os dados do produto existente
    
    # TODO DELETE
    # Implementar todo o método de delete
    # - simplesmente remover um produtdo do banco
