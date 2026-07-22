# Imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar archivos de la app al contenedor
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer el puerto de Flask
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "appMain.py"]
