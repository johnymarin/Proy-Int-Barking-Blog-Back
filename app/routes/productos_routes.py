from fastapi import APIRouter
from typing import Optional
from app.config.db_azuresql_config import azuresql_conn
from app.models.hijole_models import tabla_productos
from app.schemas.producto_schemas import Producto

db_conn = azuresql_conn
hijole_producto_router = APIRouter()

@hijole_producto_router.post("/c/")
def create_producto(producto: Producto):
    producto_a_crear = {
        "codigo_prd": producto.codigo_prd,
        "descripcion": producto.descripcion,
        "costo_producto": producto.costo_producto,
        "cantidad_producto": producto.cantidad_producto,
        "tipo_producto": producto.tipo_producto
                        }
    producto_creado = db_conn.execute(tabla_productos.insert().values(producto_a_crear))
    return db_conn.execute(tabla_productos.select().where(
        tabla_productos.c.codigo_prd == producto_creado.lastrowid
    )).first()