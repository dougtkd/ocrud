import logging
import sqlite3

# model do produto
# storage devolve e recebe ProductModel, mas ele não lê as regras de negócio (papel do service)
from models.product import ProductModel

class ProductStorage:
    """
    Classe da camada do storage, digamos que seria a camada mais baixa do nosso sistema!
    - conecta ao banco de dados
    - cria estrutura de tabela
    - insere, atualiza, busca e deleta produtos
    """
    def __init__(self):
        """
        constructor do storage
        - abre conexão com banco SQLite garantindo que a estrutura do banco exista
        """
        # cria o arquivo do banco de dados SQLite
        # o check_same_thread=False vai permitir que a conexão seja usada em mais de uma linha de execução (thread)
        self.conn = sqlite3.connect("products-database.sqlite", check_same_thread=False)

        # cria a tabela ao iniciar a aplicação
        self.__createDataBase()

    def __createDataBase(self):
        """
        Método que cria toda estrutura do banco
        - cria a tabela de produtos
        """
        if self.conn is None:
            logging.error(f"[PRODUCT-STORAGE] Connection error!")
        
        try:
            # TODO Create Database struct
            # - criar a tabela products
            # - definir as colunas (id, price, stock, name)
            # - fazer programação defensiva usando CREATE TABLE IF NOT EXISTS
            
            logging.debug(f"[PRODUCT-STORAGE] Creating Products table...")
        except Exception as error: 
            logging.error(f"[PRODUCT-STORAGE] Fail to create table: {error}")      

            # retorna o erro pro camarada que chamou
            raise error     

    def insert(self, product: ProductModel) -> int:
        """
        Método que insere produto no banco
        1. recebe um ProductModel
        2. extrai os dados do model
        3. executa o insert 
        4. retorna o id do produto salvo
        """
        try:
            # TODO Insert product into database
            # - criar um comando SQL insert
            # - executar com cursor.execute()
            # - salvar alterações com conn.commit()
            # - conseguir o id gerado com cursor.lastrowid
            
            logging.debug(f"[PRODUCT-STORAGE] Product inserted with ID {id}")
            return id
        except Exception as error:
            logging.error(f"[PRODUCT-STORAGE] Fail to insert product: {error}")
            raise error
    
    def get(self) -> list:
        """
        Método que retorna todos os produtos que foram cadastrados no banco
        1. deve executar SELECT * FROM products
        2. percorre pelos resultados
        3. converte para ProductModel
        4. retorna lista de produtos
        """
        try:
            # TODO Retrieve all products from database
            # - executar SELECT no banco
            # - converter resultado na lista de ProductModel
            # - salvar no ret
            
            logging.debug(f"[PRODUCT-STORAGE] Retrieved {len(ret)} products")
            
            return ret
            
        except Exception as error:
            logging.error(f"[PRODUCT-STORAGE] Fail to get products: {error}")
            raise error
    
    def getById(self, id: int) -> ProductModel:
        """
        Método que retorna um produto específico pelo id
        1. recebe o id do produto
        2. executa SELECT com WHERE id
        3. vai converter o resultado em ProductModel
        4. retorna produto
        """
        # variável que vai salvar o produto encontrado!
        ret = {}
        try:
            # TODO Retrieve product by ID from database
            # - executar o SELECT WHERE id
            # - verificar se encontrou resultado
            # - criar ProductModel

            logging.debug(f"[PRODUCT-STORAGE] Retrieved Product ID:{id}")
            return ret
        except Exception as error:
            logging.error(f"[PRODUCT-STORAGE] Fail to get product by ID: {error}")
            raise error
        
    # TODO UPDATE
    # Implementar todo o método de UPDATE
    # - atualizar os dados de um produto já existente no banco
    
    # TODO DELETE
    # Implementar todo o método DELETE
    # - remover um produto no banco pelo id
