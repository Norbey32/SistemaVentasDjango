# Usa la imagen oficial de Ubuntu como base
FROM ubuntu:22.04

# Evita preguntas interactivas durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instala paquetes esenciales (Python, pip, PostgreSQL cliente, build-essential)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    postgresql-client \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Establece python3 como el comando predeterminado de python
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# Establece el directorio de trabajo
WORKDIR /usr/src/app

# Copia los archivos de requerimientos e instala las dependencias de Python
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto 8000
EXPOSE 8000

# Comando para iniciar la aplicación (ejecuta collectstatic y luego Gunicorn)
# ¡REEMPLAZA <nombre_proyecto> con el nombre de tu carpeta de settings.py!
CMD python manage.py collectstatic --noinput && gunicorn <nombre_proyecto>.wsgi:application --bind 0.0.0.0:8000