from pymongo import MongoClient
from src.config import MONGO_URI, DB_NAME

def init_mongo():
    try:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        # Crear índices en la colección de registros de empresas
        db["company_records"].create_index("id", unique=True)
        print("Base de datos inicializada correctamente.")
    except Exception as err:
        print(f"Error al inicializar la base de datos: {err}")

if __name__ == "__main__":
    init_mongo()
