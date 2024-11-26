import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

if not MONGO_URI or not MONGO_DB_NAME:
    raise ValueError("Mongo URI or Database name is not set in the environment variables.")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

def insert_data(company_data):
    """
    Función para insertar datos de la empresa en la base de datos MongoDB.
    """
    collection = db.companies
    collection.insert_one(company_data)
