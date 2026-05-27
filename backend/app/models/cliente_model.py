from pydantic import BaseModel
from typing import Optional

class ClienteIn(BaseModel):
    nombre: str
    telefono: str
    correo: str
    direccion: str

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[str] = None
    direccion: Optional[str] = None