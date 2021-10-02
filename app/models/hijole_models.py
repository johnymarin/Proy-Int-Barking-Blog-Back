from enum import auto

from sqlalchemy import Table, Column, INTEGER, VARCHAR, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from app.config.db_azuresql_config import meta, engine

empleado = [
    Column("cedula", VARCHAR(20), primary_key=True, autoincrement=False),
    Column("nombre", VARCHAR(32), primary_key=False, autoincrement=False),
    Column("jornal", DECIMAL, primary_key=False, autoincrement=False)
]

tabla_domiciliaros = Table(
    "domiciliario",
    meta,
    Column("cedula", VARCHAR(20), primary_key=True, autoincrement=False),
    Column("nombre", VARCHAR(32), primary_key=False, autoincrement=False),
    Column("jornal", DECIMAL, primary_key=False, autoincrement=False)
)

tabla_meseros = Table(
    "mesero",
    meta,
    Column("cedula", VARCHAR(20), primary_key=True, autoincrement=False),
    Column("nombre", VARCHAR(32), primary_key=False, autoincrement=False),
    Column("jornal", DECIMAL, primary_key=False, autoincrement=False)
)

tabla_cocineros = Table(
    "cocinero",
    meta,
    Column("cedula", VARCHAR(20), primary_key=True, autoincrement=False),
    Column("nombre", VARCHAR(32), primary_key=False, autoincrement=False),
    Column("jornal", DECIMAL, primary_key=False, autoincrement=False),
    Column("especialidad", VARCHAR(20), ForeignKey("especialidad.codigo_especialidad"))
)

tabla_especialidad = Table(
    "especialidad",
    meta,
    Column("codigo_plato", VARCHAR(20), ForeignKey("plato.codigo"), primary_key=True),
    Column("cedula_cocinero", VARCHAR(20), ForeignKey("cocinero.cedula"), primary_key=True),
    Column("codigo_especialidad", VARCHAR(20), primary_key=True)
)

tabla_plato = Table(
    "plato",
    meta,
    Column("codigo", VARCHAR(20), primary_key=True),
    #Column("numero_pedido", VARCHAR(20), ForeignKey("pedido.numero_pedido")),
    Column("numero_pedido", VARCHAR(20)),
    Column("codigo_ingrediente", VARCHAR(20)),
    Column("cantidad", INTEGER()),
    Column("precio_total", DECIMAL())
)

tabla_productos = Table(
    "producto",
    meta,
    Column("codigo_prd", VARCHAR(20), primary_key=True),
    Column("descripcion", VARCHAR(20)),
    Column("costo_producto", DECIMAL()),
    Column("cantidad_producto", INTEGER()),
    Column("tipo_producto", VARCHAR(20))
)

tabla_clientes = Table(
    "cliente",
    meta,
    Column("cedula", VARCHAR(20), primary_key=True),
    Column("nombre", VARCHAR(20)),
    Column("ciudad", VARCHAR(20)),
    Column("telefono", VARCHAR(20))
)

meta.create_all(engine)