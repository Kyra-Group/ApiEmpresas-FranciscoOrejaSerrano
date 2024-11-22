from pymongo import MongoClient
from src.config import MONGO_URI, DB_NAME

def get_mongo_client():
    try:
        return MongoClient(MONGO_URI)
    except Exception as err:
        raise Exception(f"Error al conectar con MongoDB: {err}")

def insert_data(collection_name, data):
    try:
        client = get_mongo_client()
        db = client[DB_NAME]
        collection = db[collection_name]
        result = collection.insert_one(data)
        return result.inserted_id
    except Exception as err:
        raise Exception(f"Error al insertar datos en MongoDB: {err}")

def find_data(collection_name, query):
    try:
        client = get_mongo_client()
        db = client[DB_NAME]
        collection = db[collection_name]
        return list(collection.find(query))
    except Exception as err:
        raise Exception(f"Error al consultar datos en MongoDB: {err}")
