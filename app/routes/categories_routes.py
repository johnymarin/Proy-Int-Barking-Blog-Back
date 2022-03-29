from fastapi import APIRouter
from typing import Optional

from requests import Response
from starlette.status import HTTP_204_NO_CONTENT

from app.config.db_azuresql_config import azuresql_conn
from app.models.blog_models import category_table
from app.schemas.category_schemas import Category

db_conn = azuresql_conn
category_router = APIRouter()

@category_router.post("/c")
def create_category(category: Category):
    category_to_create = {
        "category_id": category.category_id,
        "category_name": category.category_name,
        "category_description": category.category_description,

                        }
    created_category = db_conn.execute(category_table.insert().values(category_to_create))

    return db_conn.execute(category_table.select().where(
        category_table.c.category_id == created_category.lastrowid
    )).first()

@category_router.get("/r/{category_id}", response_model=Category)
def read_category(category_id: str):
    category_found = db_conn.execute(category_table.select().where(
        category_table.c.category_id == category_id)).first()
    return category_found

@category_router.put("/u/{category_id}", response_model=Category)
def update_category(category_id: str, category: Category):
    updated_category = db_conn.execute(category_table.update()
                                           .values(category_name=category.category_name,
                                                   category_description=category.category_description
                                                   )
                                           .where(category_table.c.category_id == category_id)
                                           )
    return db_conn.execute(category_table.select()
                           .where(category_table.c.category_id == updated_category.category_id)
                           ).first()

@category_router.delete("/d/{category_id}",
                        status_code=HTTP_204_NO_CONTENT)
def delete_category(category_id: str):
    db_conn.execute(category_table.delete()
                    .where(category_table.c.category_id == category_id)
                    )
    return db_conn.execute(category_table.select()
                           .where(category_table.c.category_id == category_id)
                           ).first()