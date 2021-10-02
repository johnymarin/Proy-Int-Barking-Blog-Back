from typing import Optional
from pydantic import BaseModel

class Producto(BaseModel):
    codigo_prd: str
    descripcion: Optional[str]
    costo_producto: Optional[float]
    cantidad_producto: Optional[int]
    tipo_producto: Optional[str]
