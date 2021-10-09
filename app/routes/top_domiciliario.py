from fastapi import APIRouter
from starlette.status import HTTP_204_NO_CONTENT

from app.config.db_azuresql_config import azuresql_conn
from app.models.hijole_models import tabla_domiciliaros
from app.schemas.empleado_schemas import Domiciliario

db_conn = azuresql_conn
hijole_domiciliario_router = APIRouter()

@hijole_domiciliario_router.post("/c")
def create_domiciliario(domiciliario: Domiciliario):
    domiciliario_a_crear = {
        "cedula": domiciliario.cedula,
        "nombre": domiciliario.nombre,
        "jornal": domiciliario.jornal,
        "placa": domiciliario.placa
    }

    domiciliario_creado = db_conn.execute(
        tabla_domiciliaros
        .insert()
        .values(domiciliario_a_crear)
    )

    return db_conn.execute(
        tabla_domiciliaros
        .select()
        .where(tabla_domiciliaros.c.cedula == domiciliario_creado.lastrowid)
    ).first()

@hijole_domiciliario_router.get("/r/{cedula}")
def read_domiciliario(cedula: str):
    domiciliario_consultado = db_conn.execute(
        tabla_domiciliaros
        .select()
        .where(tabla_domiciliaros.c.cedula == cedula)
    ).first()
    return domiciliario_consultado

@hijole_domiciliario_router.get("/top")
def get_top_five():
    return db_conn.execute(
        tabla_domiciliaros
        .select()
        .order_by(tabla_domiciliaros.c.jornal)
        .limit(5)
    ).fetchall()

@hijole_domiciliario_router.put("/u/{cedula}")
def update_domiciliario(cedula: str, domiciliario: Domiciliario):
    domiciliaro_actualizado = db_conn.execute(
        tabla_domiciliaros
        .update()
        .values(
            nombre=domiciliario.nombre,
            jornal=domiciliario.jornal,
            placa=domiciliario.placa
        )
        .where(tabla_domiciliaros.c.cedula == cedula)
    )

    return db_conn.execute(
        tabla_domiciliaros
        .select()
        .where(tabla_domiciliaros.c.cedula == domiciliaro_actualizado.cedula)
    )

@hijole_domiciliario_router.delete("/d/{cedula}", status_code=HTTP_204_NO_CONTENT)
def delete_domiciliario(cedula: str):
    db_conn.execute(
        tabla_domiciliaros
        .delete()
        .where(tabla_domiciliaros.c.cedula == cedula)
    )

    return db_conn.execute(
        tabla_domiciliaros
        .select()
        .where(tabla_domiciliaros.c.cedula == cedula)
    ).first()

