from sqlalchemy import Column, Integer, String
from .database import Base

class Personaje(Base):
    __tablename__ = "personaje"
    
    id = Column(String, primary_key=True, index=True)
    rol = Column(String, nullable=False)
    profesion = Column(String, nullable=False)
    caracteristicas = Column(String, nullable=False)
    imagen = Column(String, nullable=False)
    
class Tecnologia(Base):
    __tablename__ = "tecnologia"
    
    nombre = Column(String, primary_key=True, index=True)
    descripcion = Column(String, nullable=False)
    aparicion = Column(String, nullable=False)
    uso = Column(String, nullable=False)
    imagen = Column(String, nullable=False)