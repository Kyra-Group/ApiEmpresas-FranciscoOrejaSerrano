from fastapi import APIRouter  # Importa APIRouter de FastAPI para crear rutas.
import requests  # Importa la librería requests para hacer solicitudes HTTP a la API externa.

router = APIRouter()  # Crea una instancia del enrutador de FastAPI, que se usará para definir las rutas.

# Define una ruta que responde a solicitudes GET en el endpoint "/companies"
@router.get("/companies")
async def get_companies():
    url = "https://random-data-api.com/api/company/random_company"  # URL de la API externa de donde obtendremos los datos de la empresa.
    companies = []  # Crea una lista vacía para almacenar las empresas obtenidas.

    try:
        # Numero de solicitudes consecutivas a la API externa para obtener datos de empresas.
        for _ in range(1):
            response = requests.get(url)  # Realiza una solicitud GET a la URL de la API externa.

            # Si la respuesta de la API es exitosa (status code 200), procesa los datos.
            if response.status_code == 200:
                company_data = response.json()  # Convierte la respuesta JSON a un diccionario Python.
                
                # Añade un nuevo diccionario con los campos 'id' y 'business_name' a la lista de empresas.
                companies.append({
                    "id": company_data["id"],  # Obtiene el 'id' de la respuesta de la API.
                    "name": company_data["business_name"]  # Obtiene el 'business_name' de la respuesta de la API.
                })
            else:
                # Si la respuesta no es exitosa (código de estado distinto de 200), devuelve un error con detalles.
                return {"error": f"No se pudo obtener los datos de las compañías. Status: {response.status_code}, Detalle: {response.text}"}

        # Si las 10 solicitudes fueron exitosas, devuelve la lista de empresas.
        return {"companies": companies}

    # Si ocurre algún error en la solicitud o el procesamiento de los datos, se captura la excepción y se devuelve un mensaje de error.
    except Exception as e:
        return {"error": f"Ocurrió un error: {str(e)}"}
