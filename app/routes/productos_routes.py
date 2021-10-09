from fastapi import APIRouter
from typing import Optional


from starlette.status import HTTP_204_NO_CONTENT

from app.config.db_azuresql_config import azuresql_conn
from app.models.hijole_models import tabla_productos
from app.schemas.producto_schemas import Producto

db_conn = azuresql_conn
hijole_producto_router = APIRouter()

@hijole_producto_router.post("/c")
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

@hijole_producto_router.get("/r/{codigo_prd}", response_model=Producto)
def read_producto(codigo_prd: str):
    producto_consultado = db_conn.execute(tabla_productos.select().where(
        tabla_productos.c.codigo_prd == codigo_prd)).first()
    return producto_consultado

@hijole_producto_router.put("/u/{codigo_prd}", response_model=Producto)
def update_producto(codigo_prd: str, producto: Producto):
    producto_actualizado = db_conn.execute(tabla_productos.update()
                    .values(descripcion=producto.descripcion,
                            costo_producto=producto.costo_producto,
                            cantidad_producto=producto.cantidad_producto,
                            tipo_producto=producto.tipo_producto)
                    .where(tabla_productos.c.codigo_prd == codigo_prd)
                    )
    return db_conn.execute(tabla_productos.select()
                           .where(tabla_productos.c.codigo_prd == producto_actualizado.codigo_prd)
                           ).first()

@hijole_producto_router.delete("/d/{codigo_prd}",
                               status_code=HTTP_204_NO_CONTENT)
def delete_producto(codigo_prd: str):
    db_conn.execute(tabla_productos.delete()
                    .where(tabla_productos.c.codigo_prd == codigo_prd)
                    )
    return db_conn.execute(tabla_productos.select()
                           .where(tabla_productos.c.codigo_prd == codigo_prd)
                           ).first()