# Imagen base
FROM python:3.13.2

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias
COPY requirements /requirements
RUN pip install -r /requirements/tareas.txt -r /requirements/usuarios.txt

# Copiar el código fuente de los microservicios
COPY tareas /app/tareas
COPY usuarios /app/usuarios

# Exponer los puertos de los dos microservicios
EXPOSE 8000 8001

# Comando para ejecutar ambos servidores
CMD ["sh", "-c", "cd /app/tareas && gunicorn --bind 0.0.0.0:8000 tareas.wsgi:application & cd /app/usuarios && gunicorn --bind 0.0.0.0:8001 usuarios.wsgi:application"]
