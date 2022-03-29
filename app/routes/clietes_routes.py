from fastapi import APIRouter
from starlette.status import HTTP_204_NO_CONTENT

from app.config.db_azuresql_config import azuresql_conn
from app.models.blog_models import tabla_clientes
from app.schemas.cliente_schemas import Cliente



db_conn = azuresql_conn
hijole_cliente_router = APIRouter()

@hijole_cliente_router.post("/c")
def create_cliente(cliente: Cliente):
    cliente_a_crear = {
        "cedula": cliente.cedula,
        "nombre": cliente.nombre,
        "ciudad": cliente.ciudad,
        "telefono": cliente.telefono
    }

    cliente_creado = db_conn.execute(tabla_clientes.insert().values(cliente_a_crear))
    return db_conn.execute(tabla_clientes.select().where(
        tabla_clientes.c.cedula == cliente_creado.lastrowid
    )).first()

@hijole_cliente_router.get("/r/{cedula}")
def read_cliente(cedula: str):
    cliente_consultado = db_conn.execute(
        tabla_clientes
        .select()
        .where(
            tabla_clientes.c.cedula == cedula
        )
    ).first()
    return cliente_consultado

@hijole_cliente_router.put("/u/{cedula}")
def update_cliente(cedula: str, cliente: Cliente):
    cliente_actualizado = db_conn.execute(
        tabla_clientes
        .update()
        .values(
            nombre=cliente.nombre,
            ciudad=cliente.ciudad,
            telefono=cliente.telefono
        )
        .where(tabla_clientes.c.cedula == cedula)
    )

    return db_conn.execute(
        tabla_clientes
        .select()
        .where(tabla_clientes.c.cedula == cliente_actualizado.cedula)
    )

@hijole_cliente_router.delete("/d/{cedula}", status_code=HTTP_204_NO_CONTENT)
def delete_cliente(cedula: str):
    db_conn.excecute(
        tabla_clientes
        .delete()
        .where(tabla_clientes.c.cedula == cedula)
    )

    return db_conn.execute(
        tabla_clientes
        .select()
        .where(tabla_clientes.c.cedula == cedula)
    ).first()
