# Despliegue de la Aplicación FastAPI con ngrok

Esta sección explica cómo desplegar tu aplicación FastAPI usando **ngrok**, una herramienta que crea túneles seguros y públicos hacia tu servidor local.

---

## Requisitos Previos

1. **Instalar ngrok**:
   - Descarga e instala ngrok desde su página oficial: [https://ngrok.com/download](https://ngrok.com/download).
   - Verifica que ngrok está instalado ejecutando el siguiente comando:
     ```bash
     ngrok version
     ```
     Deberías ver la versión instalada de ngrok.

2. **Aplicación FastAPI configurada**:
   - Asegúrate de que tu aplicación FastAPI está funcionando localmente.
   - Normalmente, puedes iniciar tu aplicación con:
     ```bash
     uvicorn app.main:app --reload
     ```
     Esto iniciará la aplicación en `http://127.0.0.1:8000`.

3. **Acceso al puerto**:
   - Asegúrate de que el puerto 8000 (u otro puerto en el que se ejecute tu aplicación) esté disponible.

---

## Configuración de ngrok

### 1. Obtener y Configurar el Authtoken
El authtoken permite autenticar tu instalación de ngrok y desbloquear funciones como túneles persistentes.

1. **Obtener tu authtoken**:
   - Ve a [ngrok dashboard](https://dashboard.ngrok.com/) e inicia sesión.
   - En la página principal, copia tu **authtoken**.

2. **Configurar el authtoken**:
   - Ejecuta el siguiente comando para configurar el authtoken en tu máquina:
     ```bash
     ngrok config add-authtoken <TU_AUTHTOKEN>
     ```
     Reemplaza `<TU_AUTHTOKEN>` con el authtoken que copiaste del dashboard.

### 2. Iniciar el túnel con ngrok
1. Inicia tu aplicación FastAPI localmente:
   ```bash
   uvicorn app.main:app --reload

2. En otra terminal, inicia ngrok para el puerto 8000:
   ```bash
   ngrok http 8000

3. ngrok generará una URL pública como:
   ```bash
   Forwarding                    https://abc123.ngrok.io -> http://127.0.0.1:8000