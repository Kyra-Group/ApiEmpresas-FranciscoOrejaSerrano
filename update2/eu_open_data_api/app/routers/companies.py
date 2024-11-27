from fastapi import APIRouter
from app.mongo_handler import insert_data, find_data
import requests

router = APIRouter(prefix="/companies", tags=["Companies"])

API_URL = "https://random-data-api.com/api/company/random_company"

@router.get("/")
async def get_companies():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            company = response.json()
            data = {
                "id": company.get("id"),
                "name": company.get("business_name")
            }
            insert_data(data)
            return {"message": "Compañía guardada exitosamente", "data": data}
        else:
            return {"error": "No se pudo obtener los datos de la API externa."}
    except Exception as e:
        return {"error": str(e)}

@router.get("/search")
async def search_companies(name: str):
    results = find_data({"name": {"$regex": name, "$options": "i"}})
    return {"results": results}
