# Imagen base
FROM python:3.12-slim

# Evitar que Python guarde archivos .pyc y use buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

# Crear directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto (incluyendo media/)
COPY . /app/

# Crear usuario no-root para ejecutar la aplicación
RUN groupadd --gid 1001 appgroup && \
    useradd --uid 1001 --gid appgroup --no-create-home appuser

# Crear directorios necesarios y asignar propiedad al usuario no-root
RUN mkdir -p staticfiles media && \
    chown -R appuser:appgroup /app && \
    chmod -R 755 media staticfiles

# Dar permisos de ejecución al entrypoint
RUN chmod +x docker-entrypoint.sh

# Cambiar al usuario no-root
USER appuser

# Exponer el puerto
EXPOSE 8000

# Usar el script de entrada
ENTRYPOINT ["./docker-entrypoint.sh"]
