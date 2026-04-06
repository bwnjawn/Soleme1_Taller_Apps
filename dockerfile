FROM python:3.12-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar uv usando pip
RUN pip install uv

# Copiar archivos y sincronizar dependencias [cite: 27, 28]
COPY . .
RUN uv sync --frozen

# Exponer puerto y ejecutar [cite: 33, 34]
EXPOSE 8000
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
