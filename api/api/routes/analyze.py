import sys
import os

# Esto añade la carpeta raíz al path de Python para que siempre encuentre los módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Ahora la importación funcionará desde cualquier lugar
from api.routes.analyze import router as analyze_router

from fastapi import FastAPI

app = FastAPI()

app.include_router(analyze_router)
