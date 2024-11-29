import os  # Importa el módulo os, que permite interactuar con el sistema operativo (incluyendo la gestión de archivos y variables de entorno).
from dotenv import load_dotenv  # Importa la función load_dotenv desde el módulo dotenv. Esto se utiliza para cargar las variables de entorno desde un archivo .env.

load_dotenv()  # Carga las variables de entorno definidas en el archivo .env en el entorno de ejecución de Python. 
              # Esto permite acceder a ellas con os.getenv().

# Recupera la variable de entorno MONGO_URI desde el archivo .env
MONGO_URI = os.getenv("MONGO_URI") 

# Recupera la variable de entorno MONGO_DB_NAME desde el archivo .env
DB_NAME = os.getenv("MONGO_DB_NAME")
