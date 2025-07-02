FROM python:3.11-slim

WORKDIR /app

# 1) Instalamos dependencias…
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) Copiamos todo el proyecto
COPY . .

# 3) Exponemos el puerto de FastAPI
EXPOSE 8000

# 4) Arrancamos la app por defecto
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]