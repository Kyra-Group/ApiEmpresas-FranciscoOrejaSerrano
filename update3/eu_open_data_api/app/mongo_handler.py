from pymongo import MongoClient  # Importa MongoClient de pymongo para interactuar con MongoDB.
from app.config import MONGO_URI, DB_NAME  # Importa la URI de conexión y el nombre de la base de datos desde el archivo de configuración.

# Se conecta a MongoDB usando la URI y el nombre de la base de datos definidos en el archivo de configuración.
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def insert_data(data):
    """
    Inserta un documento en la colección 'companies' de MongoDB.

    :param data: El diccionario de datos que se va a insertar en la colección.
    :raises ValueError: Si ocurre un error al intentar insertar los datos en la base de datos.
    """
    try:
        # Inserta un único documento en la colección 'companies'.
        db["companies"].insert_one(data)
    except Exception as e:
        # Si ocurre un error, lanza una excepción con el mensaje de error.
        raise ValueError(f"Error al insertar datos: {e}")

def find_data(query):
    """
    Busca documentos en la colección 'companies' de MongoDB que coincidan con la consulta.

    :param query: El diccionario de consulta para buscar en la colección.
    :return: Lista de documentos que coinciden con la consulta.
    :raises ValueError: Si ocurre un error al intentar buscar los datos en la base de datos.
    """
    try:
        # Encuentra todos los documentos que coinciden con la consulta y los devuelve como una lista.
        return list(db["companies"].find(query))
    except Exception as e:
        # Si ocurre un error, lanza una excepción con el mensaje de error.
        raise ValueError(f"Error al buscar datos: {e}")
