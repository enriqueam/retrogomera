from fastapi import FastAPI
from app.database import engine, Base
from app.controllers import router

app = FastAPI()

# Crear las tablas en la base de datos si no existen
print("🔧 Creando tablas en PostgreSQL...")
Base.metadata.create_all(bind=engine)

# Incluir las rutas de la API
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Bienvenido a RetroGomera con FastAPI!"}
