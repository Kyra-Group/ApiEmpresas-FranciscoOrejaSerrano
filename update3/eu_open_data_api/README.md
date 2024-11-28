# API para Datos Públicos de Empresas

## Descripción

Esta API permite obtener datos de empresas desde una API pública, almacenarlos en una base de datos MongoDB y consultarlos. Utiliza FastAPI como framework principal y MongoDB Atlas como base de datos. El objetivo principal es consumir datos externos y ponerlos a disposición mediante endpoints bien definidos.

---

## Características

- **Integración con API pública**: Obtiene datos desde [Random Data API](https://random-data-api.com/).
- **Almacenamiento persistente**: Los datos se almacenan en MongoDB.
- **Búsqueda flexible**: Endpoint para buscar compañías por nombre.
- **Framework moderno**: FastAPI proporciona un rendimiento rápido y una documentación interactiva.

---

## Requisitos

- **Python**: Versión 3.10 o superior.
- **MongoDB Atlas**: O una instancia local de MongoDB.
- **Dependencias**: Instaladas desde `requirements.txt`.

---

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/eu_open_data_api.git
cd eu_open_data_api
