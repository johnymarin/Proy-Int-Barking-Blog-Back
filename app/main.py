from typing import Optional

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.articles_routes import article_router
from app.routes.categories_routes import category_router
from app.routes.clientes_routes import hijole_cliente_router
from app.routes.domiciliario_routes import hijole_domiciliario_router
#from app.config.db_azuresql_config import meta, engine

# ToDo: remove commented lines
#meta.create_all(engine)

#os.environ['http_proxy'] = os.environ.get('IPB_HTTP', '')
#os.environ['https_proxy'] = os.environ.get('IPB_HTTPS', '')

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

os.environ['http_proxy'] = os.environ.get('IPB_HTTP', '')
os.environ['https_proxy'] = os.environ.get('IPB_HTTPS', '')

app.include_router(article_router,prefix="/article", tags=["Blog"])
app.include_router(category_router, prefix="/category", tags=["Blog"])
app.include_router(hijole_cliente_router,prefix="/clientes", tags=["Clientes"])
app.include_router(hijole_domiciliario_router,prefix="/domiciliarios", tags=["Domiciliario"])
