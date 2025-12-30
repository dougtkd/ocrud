import json 

class ProductModel:
    """
    Essa classe é responsável por representar um produto no sistema.

    - Quais dados o produto possui
    - Como é a organização dos dados
    - Como o produto pode ser convertido pra dict ou JSON

    Vale freezar que o Model JAMAIS acessa o banco de dados e não contém regra de negócio.. serve apenas para representar os dados do produto!
    """
    def __init__(self, id, name, price, stock):
    """
    Construtor do produto! 

    -Vamos atribuir características que o produto deve ter: id, nome, preço
    """
        # TODO
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        # - atributos definidos!

    def toDict(self) -> dict:
        """
        Método que traduz o ProductModel em dicionário Python!
        - pega o objeto e escreve as informações
        """
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

    def toJson(self) -> str:
        """
        Esse método converte o ProductModel para uma string JSON!

        - retorna dados pela API
        - gera logs
        """
        # transforma as informações do dicionário em texto
        return json.dumps(self.toDict()) 
