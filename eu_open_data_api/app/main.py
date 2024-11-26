from fastapi import FastAPI
from app.routers import companies

app = FastAPI()

# Registra las rutas
app.include_router(companies.router)
