# API para Datos Públicos de Empresas

Esta API proporciona datos públicos relacionados con empresas y startups utilizando una API externa. Los datos se almacenan en una base de datos MongoDB y se pueden consumir a través de un endpoint.

---

## Características

- **Consulta de empresas:** Obtiene datos de 10 empresas de una API pública externa y los almacena en MongoDB.
- **Base de datos:** Uso de MongoDB Atlas para almacenamiento.
- **Framework:** Desarrollada con FastAPI.
- **Despliegue:** Configuración para despliegue en Heroku y CI/CD con GitHub Actions.

---

## Instalar dependencias

python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
pip install -r requirements.txt


---

##  Inicializar la base de datos

python -m app.init_mongo

---

## Iniciar el servidor

uvicorn app.main:app --reload

---

## Endpoints

GET /
Verifica que la API está activa. Respuesta:

{
    "message": "API para datos públicos de empresas"
}

GET /companies

Obtiene empresas desde una API externa y muestra los datos en el formato:

{
    "companies": [
        {"id": 1, "name": "Empresa 1"},
        {"id": 2, "name": "Empresa 2"}
    ]
}

---

## Despliegue en Heroku

Configuración de Heroku

1. Inicia sesión en Heroku:

heroku login

2. Crea una nueva aplicación:

heroku create <nombre-de-tu-aplicacion>

3. Configura las variables de entorno en Heroku:

heroku config:set MONGO_URI="<tu-uri-de-mongodb>"
heroku config:set MONGO_DB_NAME="<tu-nombre-de-base-de-datos>"

4. Despliega la aplicación:

git push heroku main

5. Accede a tu aplicación en:

https://<nombre-de-tu-aplicacion>.herokuapp.com/

---