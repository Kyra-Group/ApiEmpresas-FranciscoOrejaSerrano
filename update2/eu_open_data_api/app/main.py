from fastapi import FastAPI
from app.routers import companiesold

app = FastAPI()

# Incluir los routers
app.include_router(companiesold.router)

@app.get("/")
def root():
    return {"message": "API para datos públicos de empresas"}
