import logging
import traceback

from storage.product import ProductStorage
from models.product import ProductModel

class ProductService:
    def __init__(self):
        self.storage = ProductStorage()

    def insert(self, prod:ProductModel) -> int:
        try:
            # TODO
            logging.debug(f"[PRODUCT-SERVICE] Insert Product: {prod.toJson()}")
        except Exception as error:
            logging.error(f"[PRODUCT-SERVICE] Fail: {error} -> {traceback.format_exc()}")

        return id
            
    def get(self) -> list:
        ret = {}
        try:
            # TODO
            logging.debug(f"[PRODUCT-SERVICE] Get all Products: {len(ret)} found")
        
        except Exception as error:
            logging.error(f"[PRODUCT-SERVICE] Fail: {error} -> {traceback.format_exc()}")
        
        return ret

    def getById(self, id:int) -> ProductModel:
        ret = {}
        try:
            # TODO
            logging.debug(f"[PRODUCT-SERVICE] Get Product by ID: {id}")
        except Exception as error:
            logging.error(f"[PRODUCT-SERVICE] Fail: {error} -> {traceback.format_exc()}")

        return ret
    
    # TODO UPDATE
    # TODO DELETE