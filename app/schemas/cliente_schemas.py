from typing import Optional
from pydantic import BaseModel

class Cliente(BaseModel):
    cedula: str
    nombre: str
    ciudad: Optional[str]
    telefono: Optional[str]