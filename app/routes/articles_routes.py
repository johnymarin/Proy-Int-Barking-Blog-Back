from fastapi import APIRouter
from typing import Optional
from app.config.db_azuresql_config import azuresql_conn
from app.models.articles_model import articles_table

db_conn = azuresql_conn
article_router = APIRouter()


@article_router.post("/c/{article_id}")
def create_article(article_id: int, q: Optional[str] = None):
    db_conn.execute(articles_table.insert().values(id=article_id), name=q)
    return "200"

@article_router.get("/r/{article_id}")
def read_article(article_id: int, q: Optional[str] = None):
    return db_conn.execute(articles_table.select().filter(articles_table.id == article_id)).fetchone()

@article_router.get("/r")
def read_articles():
    return db_conn.execute(articles_table.select()).fetchall()


@article_router.put("/u/{article_id}")
def update_article(article_id: int, q: Optional[str] = None):
    article_to_update = db_conn.execute(articles_table.select().filter(articles_table.id == article_id)).fetchone()
    db_conn.execute(articles_table.select().where(articles_table.c.id == article_to_update.id))
    return "200"

@article_router.delete("/d/{article_id}")
def delete_article(article_id: int, q: Optional[str] = None):
    pass