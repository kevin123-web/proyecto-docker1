# Proyecto-docker1
El proyecto consiste en una aplicación web que utiliza la API de Imagga para analizar imágenes y distribuirlas según sus características.

# Descripción del Proyecto
El objetivo principal de esta aplicación es proporcionar una interfaz web intuitiva para que los usuarios puedan analizar las imágenes y obtener análisis detallados sobre su contenido utilizando la API de Imagga. La aplicación permite:

- Analizar imágenes desde el dispositivo local.
- Enviar las imágenes a la API de Imagga para su análisis.
- Mostrar los resultados del análisis, incluidas etiquetas, colores predominantes y cualquier otra información - relevante proporcionada por la API.
- Distribuir las imágenes en diferentes categorías o etiquetas basadas en los resultados del análisis.

# Ejecución del Proyecto
Sigue las instrucciones proporcionadas en el README.md del proyecto para configurar y ejecutar la aplicación en tu entorno local.

# Tecnologías Utilizadas
- Python: Utilizado para el desarrollo del backend de la aplicación.
- Flask: Framework de Python utilizado para crear la aplicación web.
- Docker: Utilizado para contenerizar la aplicación y facilitar su despliegue en diferentes entornos.
- Imagga API: Utilizada para el análisis de imágenes y la obtención de información detallada sobre su
  contenido.
  
# 1.- Clonar el Repositorio  
 Git clone https://github.com/kevin123-web/proyecto-docker1
# 2.- Configurar las Credenciales de Immaga
Obtén tus credenciales de Immaga en el siguiente enlace: (https://docs.imagga.com/#getting-started-signup) una vez realizado reemplace sus credenciales en API_KEY=TU_API_KEY y API_SECRET_KEY=TU_SECRET_KEY remplazarlas en el app.py y index.html .
# 3.- Dirigirse a la carpeta del aplicativo
Dirigirse a la carpeta del aplicativo ejemplo cd proyecto-docker
# 4.- Verificar el archivo del dockerfile
Primero se verifica el archivo del Dockerfile antes de la creación de la imagen en docker cabe recalcar que solo debe verificarlo que este clonado junto al proyecto , los requirements.txt y docker-compose.yml ya estan configurados e  igual que Dockerfile, si en caso no se encuentra puede crear el DockerFile aqui un ejemplo como deberia verse el Dockerfile: 
## Establece el directorio de trabajo en el contenedor
WORKDIR /app

## Copia el archivo de requisitos al directorio de trabajo
COPY requirements.txt requirements.txt

## Actualiza pip e instala las dependencias en el mismo paso
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

## Copia la aplicación al contenedor
COPY . .

## Establece las variables de entorno necesarias
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

## Expone el puerto en el que correrá la aplicación Flask
EXPOSE 5000

## Comando para correr la aplicación
CMD ["flask", "run"]

# 5.- Crear la imagen de docker 
Se debe tener descargado el docker para crear la imagen con el siguiente comando se crea la imagen "docker build -t flask-app ."   .

# 6.- Compilación de la aplicación
Con el siguiente comando se ejecuta la imagen que hemos creado "docker run -p 5000:5000 flask-app" . 


