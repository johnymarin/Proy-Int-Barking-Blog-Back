from fastapi import APIRouter
from typing import Optional
from app.config.db_azuresql_config import azuresql_conn
from app.models.products_model import products_table

db_conn = azuresql_conn
product_router = APIRouter()


@product_router.post("/c/{product_id}")
def create_product(product_id: int, q: Optional[str] = None):
    db_conn.execute(products_table.insert().values(id=product_id), name=q)
    return "200"

@product_router.get("/r/{product_id}")
def read_product(product_id: int, q: Optional[str] = None):
    return db_conn.execute(products_table.select().filter(products_table.id == product_id)).fetchone()

@product_router.get("/r")
def read_products():
    return db_conn.execute(products_table.select()).fetchall()


@product_router.put("/u/{product_id}")
def update_product(product_id: int, q: Optional[str] = None):
    product_to_update = db_conn.execute(products_table.select().filter(products_table.id == product_id)).fetchone()
    db_conn.execute(products_table.select().where(products_table.c.id == product_to_update.id ))
    return "200"

@product_router.delete("/d/{product_id}")
def delete_product(product_id: int, q: Optional[str] = None):
    pass