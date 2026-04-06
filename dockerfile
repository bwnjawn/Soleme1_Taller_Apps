# 1. Utilizar una imagen base de Python 
FROM python:3.12-slim

# 2. Instalar uv en el contenedor para gestionar el entorno 
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 3. Establecer el directorio de trabajo
WORKDIR /app

# 4. Copiar los archivos necesarios al contenedor [cite: 27]
# Esto incluye main.py, pyproject.toml y uv.lock
COPY . /app

# 5. Instalar las dependencias de Python utilizando uv [cite: 28]
# Sincroniza el entorno basándose en tu archivo pyproject.toml
RUN uv sync --frozen

# 6. Exponer el puerto 8000 [cite: 21, 33]
EXPOSE 8000

# 7. Definir el comando para ejecutar la aplicación con uvicorn 
# Usamos 'uv run' para asegurar que se ejecute dentro del entorno virtual creado
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]