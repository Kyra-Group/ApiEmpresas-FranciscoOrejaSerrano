import os
from dotenv import load_dotenv

# Carga las variables de entorno desde un archivo .env
load_dotenv()

# Configuración de la API de Datos Abiertos de la Unión Europea
API_BASE_URL = "https://data.europa.eu/api/hub/search"

# Configuración de la base de datos MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "company_data")
