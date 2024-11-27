from pymongo import MongoClient
from app.config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def insert_data(data):
    try:
        db["companies"].insert_one(data)
    except Exception as e:
        raise ValueError(f"Error al insertar datos: {e}")

def find_data(query):
    try:
        return list(db["companies"].find(query))
    except Exception as e:
        raise ValueError(f"Error al buscar datos: {e}")
