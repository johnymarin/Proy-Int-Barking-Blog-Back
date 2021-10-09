from typing import Optional
from pydantic import BaseModel

class Empleado(BaseModel):
    cedula: str
    nombre: str
    jornal: float


class Cocinero(Empleado):
    especialidad: str

class Domiciliario(Empleado):
    placa: str

class mesero(Empleado):
    turno: str
