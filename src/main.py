from src.api_client import fetch_company_data
from src.mongo_handler import insert_data

def main():
    print("Buscando datos relacionados con 'companies'...")
    search_results = fetch_company_data("companies")
    
    # Insertar resultados en MongoDB
    records = search_results.get("result", {}).get("records", [])
    for record in records:
        print(f"Insertando registro con ID: {record.get('id')}")
        insert_data("company_records", record)
    
    print("Búsqueda completada e información almacenada en MongoDB.")

if __name__ == "__main__":
    main()
