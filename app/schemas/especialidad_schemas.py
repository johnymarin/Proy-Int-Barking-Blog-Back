from typing import Optional
from pydantic import BaseModel

class Especialidad(BaseModel):
    codigo_plato: str
    cedula_cocinero: str
    codigo_especialidad: str