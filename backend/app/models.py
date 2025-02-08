from sqlalchemy import Column, Integer, String, TIMESTAMP
from app.database import Base  # Importamos la base para definir modelos
from datetime import datetime, timezone

# Modelo para la tabla de imágenes
class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    path = Column(String, nullable=False)  # Ruta en el sistema de archivos
    description = Column(String, nullable=True)
    upload_date = Column(TIMESTAMP, default=datetime.now(timezone.utc) )
    file_size = Column(Integer, nullable=True)  # Tamaño en bytes
    file_type = Column(String, nullable=True)  # Tipo de imagen (MIME)
    width = Column(Integer, nullable=True)  # Ancho en píxeles
    height = Column(Integer, nullable=True)  # Alto en píxeles