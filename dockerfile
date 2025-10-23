# Usa una imagen base de Python oficial
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Instala dependencias del sistema operativo (necesarias para psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia los archivos de requerimientos e instala dependencias de Python
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto donde Gunicorn correrá
EXPOSE 8000

# Comando para recolectar estáticos y luego iniciar Gunicorn
# Reemplaza <nombre_proyecto> con el nombre real de tu carpeta (ej. sistema_ventas)
CMD python manage.py collectstatic --noinput && gunicorn <nombre_proyecto>.wsgi:application --bind 0.0.0.0:8000