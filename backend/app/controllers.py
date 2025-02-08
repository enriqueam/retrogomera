from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Image
from pathlib import Path
import shutil
from PIL import Image as PILImage

router = APIRouter()

UPLOAD_DIR = Path("/app/uploads")


@router.get("/imagenes")
def obtener_imagenes(db: Session = Depends(get_db)):
    return db.query(Image).all()


def get_image_metadata(file):
    """ Obtiene dimensiones y tipo MIME de la imagen """
    file_size = len(file.file.read())  # Tamaño en bytes
    img = PILImage.open(file.file)
    width, height = img.size
    file_type = img.format.lower()
    return width, height, file_size, file_type


@router.post("/upload/")
def upload_image(file: UploadFile, description = "", 
                 db: Session = Depends(get_db)):
    image_path = UPLOAD_DIR / file.filename
    width, height, file_size, file_type = get_image_metadata(file)
    try:
        with image_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        return {"error": f"Error al guardar el archivo: {str(e)}"}

    new_image = Image(
        name=file.filename,
        path=str(image_path),
        file_size=file_size,
        file_type=file_type,
        width=width,
        height=height
    )
    try:
        db.add(new_image)
        db.commit()
        db.refresh(new_image)
    except:
        return {"error": "Error al guardar la imagen en la BBDD"}
    return {"message": "Imagen subida correctamente."}
