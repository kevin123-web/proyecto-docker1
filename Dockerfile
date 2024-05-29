# Usa una imagen base oficial de Python
FROM python:3.9-buster

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos al directorio de trabajo
COPY requirements.txt requirements.txt

# Actualiza pip e instala las dependencias en el mismo paso
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia la aplicación al contenedor
COPY . .

# Establece las variables de entorno necesarias
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expone el puerto en el que correrá la aplicación Flask
EXPOSE 5000

# Comando para correr la aplicación
CMD ["flask", "run"]
