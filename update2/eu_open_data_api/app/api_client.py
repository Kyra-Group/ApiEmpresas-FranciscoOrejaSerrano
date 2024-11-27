import requests
from app.config import API_BASE_URL

def fetch_company_data(query: str):
    """
    Busca datos relacionados con compañías en la API pública.

    :param query: Término de búsqueda.
    :return: Diccionario con los resultados de la búsqueda.
    """
    try:
        params = {"query": query, "format": "json"}
        response = requests.get(API_BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as http_err:
        raise Exception(f"Error HTTP al consumir la API: {http_err}")
    except Exception as err:
        raise Exception(f"Error al consumir la API: {err}")
