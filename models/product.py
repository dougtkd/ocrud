import json 

class ProductModel:
    def __init__(self):
        # TODO
        pass

    def toJson(self) -> str:
        return json.dumps(self.toDict())