from pymongo import MongoClient  # Se importa MongoClient desde pymongo, que es la clase que permite conectarse a MongoDB.
from app.config import MONGO_URI, DB_NAME  # Se importa MONGO_URI y DB_NAME desde el archivo de configuración para conectar con la base de datos.

def init_mongo():
    try:
        # Intentamos conectarnos a MongoDB usando las variables de entorno definidas en el archivo de configuración.
        client = MongoClient(MONGO_URI)  # Creamos un cliente de MongoDB utilizando la URI de conexión
        db = client[DB_NAME]  # Seleccionamos la base de datos que se especifica en DB_NAME.

        # Creamos un índice único para el campo "id" en la colección "companies". Esto garantiza que no haya duplicados en los ids.
        db["companies"].create_index("id", unique=True)

        # Si todo sale bien, imprimimos que la base de datos se inicializó correctamente.
        print("Base de datos inicializada correctamente.")
    except Exception as err:
        # Si ocurre un error durante el proceso, lo capturamos y mostramos el mensaje de error.
        print(f"Error al inicializar la base de datos: {err}")

# Este bloque asegura que la función init_mongo() se ejecute solo si este archivo es ejecutado directamente, no si se importa en otro archivo.
if __name__ == "__main__":
    init_mongo()
