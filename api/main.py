from fastapi import FastAPI
# Como main.py y la carpeta 'rutas' están en la misma carpeta 'api', 
# el import es directo:
from rutas.analizar import router as analyze_router

app = FastAPI()

# Incluimos el router que importamos
app.include_router(analyze_router)
