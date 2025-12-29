import logging
import sqlite3
from models.product import ProductModel

class ProductStorage:
    def __init__(self):
        self.conn = sqlite3.connect("products-database.sqlite", check_same_thread=False)
        self.__createDataBase()

    def __createDataBase(self):
        if self.conn is None:
            logging.error(f"[PRODUCT-STORAGE] Connection error!")
        
        try:
            # TODO Create Database struct
            logging.debug(f"[PRODUCT-STORAGE] Creating Products table...")
        except Exception as error: 
            logging.error(f"[PRODUCT-STORAGE] Fail to create table: {error}")      
            raise error     

    def insert(self, product: ProductModel) -> int:
        try:
            # TODO Insert product into database
            logging.debug(f"[PRODUCT-STORAGE] Product inserted with ID {id}")
            return id
        except Exception as error:
            logging.error(f"[PRODUCT-STORAGE] Fail to insert product: {error}")
            raise error
    
    def get(self) -> list:
        try:
            # TODO Retrieve all products from database
            logging.debug(f"[PRODUCT-STORAGE] Retrieved {len(ret)} products")
            return ret
        except Exception as error:
            logging.error(f"[PRODUCT-STORAGE] Fail to get products: {error}")
            raise error
    
    def getById(self, id: int) -> ProductModel:
        ret = {}
        try:
            # TODO Retrieve product by ID from database

            logging.debug(f"[PRODUCT-STORAGE] Retrieved Product ID:{id}")
            return ret
        except Exception as error:
            logging.error(f"[PRODUCT-STORAGE] Fail to get product by ID: {error}")
            raise error
        
    # TODO UPDATE
    # TODO DELETE