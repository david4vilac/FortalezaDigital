from pydantic import BaseModel
from typing import Optional
###Registro Prueba###
class Personaje(BaseModel):
    id: str
    rol: str
    profesion: str
    caracteristicas: str
    imagen: str    
    
    class Config:
        orm_mode = True
        
class Personaje(BaseModel):
    nombre: str
    descripcion: str
    aparicion: str
    uso: str
    imagen: str    
    
    class Config:
        orm_mode = True