from fastapi import APIRouter
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

from app.config.db_azuresql_config import azuresql_conn
from app.models.hijole_models import tabla_domiciliaros
from app.schemas.empleado_schemas import Domiciliario

db_conn = azuresql_conn
hijole_domiciliario_router = APIRouter()

@hijole_domiciliario_router.get("/top", response_model=List[Domiciliario])
def get_top_five():
    return db_conn.execute(
        tabla_domiciliaros
        .select()
        .order_by(tabla_domiciliaros.c.jornal)
        .limit(5)
    ).fetchall()

