from typing import Optional

from fastapi import FastAPI
from app.routes.products_routes import product_router
from app.routes.productos_routes import hijole_producto_router
#from app.config.db_azuresql_config import meta, engine

#meta.create_all(engine)


app = FastAPI()

app.include_router(product_router, prefix="/restaurante", tags=["Restaurante"])
app.include_router(hijole_producto_router, prefix="/productos", tags=["Producto"])
