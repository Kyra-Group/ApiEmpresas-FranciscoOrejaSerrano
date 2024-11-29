from fastapi import FastAPI  # Importa la clase FastAPI que es el framework principal para crear la API.
from app.routers import companies  # Importa el router de empresas desde la carpeta app/routers, donde se define la lógica para manejar las solicitudes de compañías.

# Crea una instancia de la aplicación FastAPI
app = FastAPI()

# Incluye el router de empresas en la aplicación. Esto agrega las rutas definidas en el archivo companies.py al API.
app.include_router(companies.router)

@app.get("/")  # Define un endpoint GET para la ruta raíz "/".
def root():
    """
    Endpoint raíz para verificar que el API está activa.
    """
    # Este endpoint responde con un mensaje simple para verificar que la API está funcionando.
    return {"message": "API para datos públicos de empresas"}
