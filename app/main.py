from typing import Optional

import os

from fastapi import FastAPI
from app.routes.articles_routes import article_router
from app.routes.categories_routes import category_router
from app.routes.clietes_routes import hijole_cliente_router
from app.routes.domiciliario_routes import hijole_domiciliario_router
#from app.config.db_azuresql_config import meta, engine

# ToDo: remove commented lines
#meta.create_all(engine)

#os.environ['http_proxy'] = os.environ.get('IPB_HTTP', '')
#os.environ['https_proxy'] = os.environ.get('IPB_HTTPS', '')

app = FastAPI()

os.environ['http_proxy'] = os.environ.get('IPB_HTTP', '')
os.environ['https_proxy'] = os.environ.get('IPB_HTTPS', '')

app.include_router(article_routerx="/article", tags=["Blog"])
app.include_router(category_router, prefix="/category", tags=["Blog"])
app.include_router(hijole_cliente_router,prefix="/clientes", tags=["Clientes"])
app.include_router(hijole_domiciliario_router,prefix="/domiciliarios", tags=["Domiciliario"])
