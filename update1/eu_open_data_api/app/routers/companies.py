from fastapi import APIRouter
import requests
from app.mongo_handler import insert_data
from typing import List

router = APIRouter()

@router.get("/companies/{company_name}")
async def get_company_data(company_name: str):
    """
    Buscar datos de startups usando la API de API Ninjas y guardarlos en MongoDB.
    """
    url = f"https://api.api-ninjas.com/v1/startups?name={company_name}"
    headers = {
        'X-Api-Key': 'CyE7ufBwYo5sp0UqCZqfKg==ovkP3SBTDyplD0oT'  # Reemplaza con tu clave de API
    }

    # Realizar la solicitud GET a la API externa
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return {"error": "No se pudo obtener los datos de la startup."}

    # Extraer los datos de la respuesta
    startup_data = response.json()

    # Almacenar los datos en MongoDB
    for startup in startup_data:
        insert_data(startup)

    return {"message": "Datos de la startup guardados exitosamente."}
