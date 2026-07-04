import sys
import os

# Agregamos la carpeta raíz al path para asegurar que 'routes' sea encontrada
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from fastapi import FastAPI
# Ahora importamos desde routes, ya que estamos dentro de la subcarpeta 'api'
from routes.analyze import router as analyze_router

app = FastAPI()

app.include_router(analyze_router)
