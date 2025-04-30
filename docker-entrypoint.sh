#!/bin/sh
set -xe

# Iniciar el servidor de FastAPI con Uvicorn usando Poetry
exec uvicorn src.main:app --workers 1 --host 0.0.0.0 --port 80 --http h11

