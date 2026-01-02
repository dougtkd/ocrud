import logging # biblioteca do Python pra registrar logs
import sqlite3 # biblioteca do Python pra usar banco de dados SQLite

# model do produto
# storage devolve e recebe ProductModel, mas ele não lê as regras de negócio (papel do service)
from models.product import ProductModel #importa o ProductModel que funciona como intérprete! Transforma dados do banco em objeto do sistema

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
        self.conexao = sqlite3.connect("products-database.sqlite", check_same_thread=False) # self.conexao é o atributo que vai guardar a conexao com o banco

        # cria a tabela ao iniciar a aplicação
        self.__createDataBase() # assim que o storage é criado, a tabela e criada junto

    def __createDataBase(self):
        """
        Método que cria toda estrutura do banco
        - cria a tabela de produtos
        """
        
        if self.conexao is None: # se a conexao não existir, retorna erro
            logging.error(f"[PRODUCT-STORAGE] Connection error!")
            return
            
        try:
            # TODO Create Database struct
            sql = self.conexao.cursor() # criamos um objeto para executar os comandos SQL 

            # executa o comando SQL
            #IF NOT EXISTS ajuda evitar erro se já existir tabela
            sql.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    price REAL,
                    stock INTEGER
                )
            """ )

            # o commit faz a confirmação no banco
            self.conexao.commit()
            
            logging.debug(f"[PRODUCT-STORAGE] Creating Products table...")
            
        except Exception as error: 
            logging.error(f"[PRODUCT-STORAGE] Fail to create table: {error}")      

            # retorna o erro pra camarada que chamou o método
            raise error     

    def insert(self, product: ProductModel) -> int:
        """
        Método que insere produto no banco
        1. recebe um ProductModel
        2. retorna o id do produto salvo no banco
        """
        try:
            # TODO Insert product into database
            sql = self.conexao.cursor() # criamos objeto pra executar comando SQL
            sql.execute(
                "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", # executa o INSERT usando (?), PLACEHOLDER marcador temporário
                (product.name, product.price, product.stock)
            )
            self.conexao.commit() # o commit faz a confirmação no banco
            
            logging.debug(f"[PRODUCT-STORAGE] Product inserted with ID {sql.lastrowid}") #lastrowid é o atributo que vai salvar o ID do produto q acabou de ser gerado
            return sql.lastrowid # retorna o ID pra quem chamou o método
            
        except Exception as error:
            logging.error(f"[PRODUCT-STORAGE] Fail to insert product: {error}")
            raise error
    
    def get(self) -> list:
        """
        Método que retorna todos os produtos que foram cadastrados no banco
        1. deve executar SELECT * FROM products
        3. retorna lista ProductModel
        """
        try:
            # TODO Retrieve all products from database
            sql = self.conexao.cursor() # criamos o objeto que executa SQL
            sql.execute("SELECT id, name, price, stock FROM products") # enviamos atraves do objeto uma instrução de consulta SQL no banco

            produtos =  [
                ProductModel(linha[0], linha[1], linha[2], linha[3]) # toda linha vira um ProductModel
                for linha in sql.fetchall() # pegue todas as linhas que o objeto encontrou e me entrega uma lista com eles. E o for percorre essa lista transformando todas linhas e ProductModel
            ]
            
            logging.debug(f"[PRODUCT-STORAGE] Retrieved {len(produtos)} products")
            return produtos # retorna a lista de produtos já convertida
            
        except Exception as error:
            logging.error(f"[PRODUCT-STORAGE] Fail to get products: {error}")
            raise error
    
    def getById(self, id: int) -> ProductModel:
        """
        Método que retorna um produto específico pelo id
        1. recebe o id do produto
        2. executa SELECT com WHERE id
        3. Se não achar, retorna None
        """
        try:
            # TODO Retrieve product by ID from database
            sql = self.conexao.cursor() # Criamos o objeto que executa SQL
            sql.execute("SELECT id, name, price, stock FROM products WHERE id = ?", (id,)) #executamos o SELECT filtrando por id

            linha = sql.fetchone() # diferente do fetchall o fetchone retorna apenas uma linha
            if not linha:
                return None # se não achou nada no banco retorna None

            produto = ProductModel(linha[0], linha[1], linha[2], linha[3]) # Converte a linha em ProductModel
            
            logging.debug(f"[PRODUCT-STORAGE] Retrieved Product ID:{id}")
            return produto 
            
        except Exception as error:
            logging.error(f"[PRODUCT-STORAGE] Fail to get product by ID: {error}")
            raise error
        
    # TODO UPDATE
    def update(self, product: ProductModel) -> bool:
        """
        Método que atualiza um produto já existente
        - retorna true se atualizado, ou false se não encontrar o id
        """
        try:
            sql = self.conexao.cursor() # Criamos o objeto que executa SQL
            sql.execute( # executamos o UPDATE com o possível id do produto
                """
                UPDATE products
                SET name = ?, price = ?, stock = ?
                WHERE id = ?
                """,
                (product.name, product.price, product.stock, product.id)
            )
            self.conexao.commit() # o commit confirma no banco

            atualiza = sql.rowcount > 0 # o atributo rowcount vai salvar a quantidade de linhas afetadas pelo update

            logging.debug(f"[PRODUCT-STORAGE] Product ID {product.id} updated")
            return atualiza

        except Exception as error:
            logging.error(f"[PRODUCT-STORAGE] Fail to update product: {error}")
            raise error
    
    # TODO DELETE
    def delete(self, id: int) -> bool:
        """
        Esse Método remove um produto do banco pelo ID
        - retorna true se deu certo, false se não encontrou
        """
        try:
            sql = self.conexao.cursor() # criamos o objeto que executa SQL
            sql.execute( # executamos a instrução de delete
                "DELETE FROM products WHERE id = ?", (id,)
            )
            self.conexao.commit() # confirmamos no banco

            remove = sql.rowcount > 0 # o atributo rowcount vai salvar a quantidade de linhas que foi removida

            logging.debug(f"[PRODUCT-STORAGE] Product ID {id} deleted")
            return remove

        except Exception as error:
            logging.error(f"[PRODUCT-STORAGE] Fail to delete product: {error}")
            raise error
