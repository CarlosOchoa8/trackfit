FROM python:3.12-slim as builder

WORKDIR /usr/src/app

# Instalar las dependencias necesarias
RUN apt-get update \
  && apt-get clean \
  && apt-get -y install libpq-dev curl

# Configurar la zona horaria
ENV TZ="America/Mexico_City"

# Copiar los archivos fuente al contenedor
COPY . .

# Instalar Poetry 1.8.3
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.8.3

# Asegurar que poetry esté en el PATH
ENV PATH="/root/.local/bin:$PATH"

# Verificar la versión de Poetry
RUN poetry --version

# Copiar los archivos pyproject.toml y poetry.lock al contenedor
COPY pyproject.toml poetry.lock ./

# Instalar las dependencias con poetry antes de exportar
RUN poetry install

# Exportar las dependencias de Poetry a requirements.txt y luego instalar con pip
RUN set -ex \
    && poetry export --without-hashes --format requirements.txt > requirements.txt \
    && pip install -r requirements.txt \
    && rm requirements.txt

# Instalar DBMate
RUN curl -fsSL -o /usr/local/bin/dbmate https://github.com/amacneil/dbmate/releases/latest/download/dbmate-linux-amd64
RUN chmod +x /usr/local/bin/dbmate

# Crear el usuario app
RUN addgroup --system app && \
    adduser --system --ingroup app app

# Copiar el código al contenedor con el usuario app
COPY --chown=app:app . .

# Copiar el script de entrada y darle permisos de ejecución
COPY --chown=app:app docker-entrypoint.sh ./
RUN chmod +x docker-entrypoint.sh

USER app

ENTRYPOINT ["./docker-entrypoint.sh"]