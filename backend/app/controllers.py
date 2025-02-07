from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Image

router = APIRouter()

@router.get("/imagenes")
def obtener_imagenes(db: Session = Depends(get_db)):
    return db.query(Image).all()

@router.post("/imagenes")
def crear_imagen(nombre: str, url: str, db: Session = Depends(get_db)):
    nueva_imagen = Image(nombre=nombre, url=url)
    db.add(nueva_imagen)
    db.commit()
    db.refresh(nueva_imagen)
    return nueva_imagen