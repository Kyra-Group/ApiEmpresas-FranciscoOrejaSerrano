import requests  # Importa el módulo requests para hacer solicitudes HTTP.
from app.config import API_BASE_URL  # Importa la URL base de la API desde la configuración.

def fetch_company_data(query: str):
    """
    Busca datos relacionados con compañías en la API pública.

    :param query: Término de búsqueda.
    :return: Diccionario con los resultados de la búsqueda.
    """
    try:
        # Define los parámetros que se enviarán en la solicitud GET a la API.
        # 'query': El término que el usuario desea buscar en la API.
        # 'format': Especifica que queremos los resultados en formato JSON.
        params = {"query": query, "format": "json"}

        # Realiza una solicitud GET a la API con los parámetros definidos.
        response = requests.get(API_BASE_URL, params=params)

        # Si la respuesta HTTP indica un error (código de estado 4xx o 5xx), se generará una excepción.
        response.raise_for_status()

        # Si la solicitud fue exitosa, retorna la respuesta en formato JSON.
        return response.json()

    except requests.HTTPError as http_err:
        # Si ocurre un error HTTP (por ejemplo, la API no está disponible o el código de respuesta es 4xx o 5xx),
        # se captura la excepción y se lanza un nuevo error con detalles del problema.
        raise Exception(f"Error HTTP al consumir la API: {http_err}")

    except Exception as err:
        # Cualquier otro tipo de error (por ejemplo, problemas de conexión o errores en la lógica)
        # se captura aquí y se lanza una excepción genérica.
        raise Exception(f"Error al consumir la API: {err}")
