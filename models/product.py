import json 

class ProductModel:
    """
    Essa classe é responsável por representar um produto no sistema.

    - Quais dados o produto possui
    - Como é a organização dos dados
    - Como o produto pode ser convertido pra dict ou JSON

    Vale freezar que o Model JAMAIS acessa o banco de dados e não contém regra de negócio.. serve apenas para representar os dados do produto!
    """
    def __init__(self):
    """
    Construtor do produto! 

    -Vamos atribuir características que o produto deve ter: id, nome, preço
    """
        # TODO
        # - Definir os atributos do produto!
        pass

    def toJson(self) -> str:
    """
    Esse método converte o ProductModel para uma string JSON!

    - retorna dados pela API
    - gera logs
    """
        # o método toDict aqui transforma o objeto em um dicionário Python! 
        return json.dumps(self.toDict()) 
