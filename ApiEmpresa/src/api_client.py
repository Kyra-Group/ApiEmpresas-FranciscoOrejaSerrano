import requests
from src.config import API_BASE_URL

def fetch_company_data(query):
    """
    Busca datos relacionados con compañías en la API de Datos Abiertos de la Unión Europea.

    :param query: Término de búsqueda.
    :return: Diccionario con los resultados de la búsqueda.
    """
    try:
        # Construir los parámetros de la solicitud
        params = {"query": query, "format": "json"}

        # Hacer la solicitud GET a la API
        response = requests.get(API_BASE_URL, params=params)
        response.raise_for_status()  # Lanza un error si el estado HTTP no es 200

        # Devolver los resultados en formato JSON
        return response.json()

    except requests.HTTPError as http_err:
        raise Exception(f"Error HTTP al consumir la API: {http_err}")
    except Exception as err:
        raise Exception(f"Error al consumir la API: {err}")
