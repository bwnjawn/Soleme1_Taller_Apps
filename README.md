# Solemne 1 - Aplicaciones y Tecnologías Web

## Descripción del Proyecto
API desarrollada con FastAPI que devuelve la fecha y hora actual en formato JSON (Año-Mes-Día Hora:Minuto:Segundo). El proyecto incluye automatización de pruebas, linting y construcción de imágenes Docker mediante un pipeline de CI/CD en GitHub Actions.

## Instrucciones de Ejecución Local

1. Asegúrese de tener instalado el gestor de paquetes `uv`.
2. Python 3.12
3. Clone el repositorio y acceda al directorio raíz del proyecto.
4. Instale las dependencias y cree el entorno virtual:
        uv sync 
5. Inicie el servidor local utilizando uvicorn:
        uv run uvicorn main:app --host 0.0.0.0 --port 8000 


## Instrucciones de Ejecución con Docker
Construir la imagen de Docker:
    docker build -t solemne-1 .
Ejecutar el contenedor mapeando el puerto 8000:
    docker run -d -p 8000:8000 --name api-time solemne-1

## Instrucciones para Testear la API
Mediante cURL:
    curl http://localhost:8000/time
Mediante Navegador Web:
    http://localhost:8000/time
Pruebas Unitarias:
    uv run pytest