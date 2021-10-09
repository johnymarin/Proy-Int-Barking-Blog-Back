from typing import Optional

import os, requests

from fastapi import FastAPI
from app.routes.products_routes import product_router
from app.routes.productos_routes import hijole_producto_router
from app.routes.clietes_routes import hijole_cliente_router
from app.routes.domiciliario_routes import hijole_domiciliario_router
#from app.config.db_azuresql_config import meta, engine

#meta.create_all(engine)

os.environ['http_proxy'] = os.environ.get('IPB_HTTP', '')
os.environ['https_proxy'] = os.environ.get('IPB_HTTPS', '')

app = FastAPI()

os.environ['http_proxy'] = os.environ.get('IPB_HTTP', '')
os.environ['https_proxy'] = os.environ.get('IPB_HTTPS', '')

#app.include_router(product_router, prefix="/restaurante", tags=["Restaurante"])
app.include_router(hijole_producto_router, prefix="/productos", tags=["Producto"])
app.include_router(hijole_cliente_router,prefix="/clientes", tags=["Clientes"])
app.include_router(hijole_domiciliario_router,prefix="/domiciliarios", tags=["Domiciliario"])
