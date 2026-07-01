FROM python:3.10

# carpeta de trabajo dentro del contenedor
WORKDIR /app

# copiar todo el proyecto al contenedor
COPY . /app

# actualizar pip
RUN pip install --upgrade pip

# instalar dependencias
RUN pip install -r requirements.txt

# abrir puerto de FastAPI
EXPOSE 8000

# correr la API
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
