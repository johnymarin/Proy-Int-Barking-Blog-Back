from sqlalchemy import Table, Column, Integer, String
from app.config.db_azuresql_config import meta, engine

products_table = Table(
    "products",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), primary_key=False, autoincrement=False)
)

meta.create_all(engine)

