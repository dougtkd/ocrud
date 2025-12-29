#!/bin/env python3

import logging
from flask import Flask, request, jsonify
from http import HTTPStatus
from datetime import datetime
import json 

from models.product import ProductModel
from services.product import ProductService

print("Starting...")

app = Flask(__name__)
service = ProductService()
logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="logs/products-service.log",
    filemode='a',
    datefmt='%H:%M:%S',
)
print("Exiting...")

def makeResponse(msg: str, args: dict = {}):
    ret = {
        "message": msg,
        "timestamp": datetime.now().isoformat()
    }

    for key in args:
        ret[key] = args[key]

    return ret

@app.route("/products", methods = ['POST'])
def insert():
    try:
        id = ""
        # TODO
        logging.debug(f"[PRODUCT-API] Request data: {request.data}")
        return makeResponse(f"All products"), HTTPStatus.NOT_IMPLEMENTED
    except Exception as error: 
        errorMsg = f"Error to try process request: Invalid request {error}"
        logging.error(f"[PRODUCT-API] {errorMsg}")
        return makeResponse(errorMsg), HTTPStatus.BAD_REQUEST

@app.route("/products", methods = ['GET'])
def get():
    ret = {}
    try:
        return makeResponse(f"All products"), HTTPStatus.NOT_IMPLEMENTED
    except Exception as error: 
        errorMsg = f"Error to try get all products: {error}"
        logging.error(f"[PRODUCT-API] {errorMsg}")
        return makeResponse(errorMsg), HTTPStatus.INTERNAL_SERVER_ERROR    

@app.route("/products/<id>", methods = ['GET'])
def getById(id):
    ret = {}
    try:
        return makeResponse(f"Product id {id}", { "data": ret.toDict() }), HTTPStatus.NOT_IMPLEMENTED
    except Exception as error: 
        errorMsg = f"Error to try get product id {id}: {error}"
        logging.error(f"[PRODUCT-API] {errorMsg}")
        return makeResponse(errorMsg), HTTPStatus.INTERNAL_SERVER_ERROR    

# TODO UPDATE
# TODO DELETE   

