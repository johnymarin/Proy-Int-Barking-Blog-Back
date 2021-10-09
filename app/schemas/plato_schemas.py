from typing import Optional
from pydantic import BaseModel

class Plato(BaseModel):
    codigo: str
    numero_pedido: str
    codigo_ingrediente:str
    cantidad: Optional[int]
    precio_total: Optional[float]
