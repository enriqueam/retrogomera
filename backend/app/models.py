from sqlalchemy import Column, Integer, String
from app.database import Base  # Importamos la base para definir modelos

# Modelo para la tabla de imágenes
class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    url = Column(String, nullable=False)
