from typing import Optional

from fastapi import APIRouter, Query

api_router = APIRouter()


@api_router.get("/items/")
async def read_items(q: Optional[str] = Query(None,
                                              min_length=3,
                                              max_length=50,
                                              regex="^fixedquery$",
                                              title="Query string",
                                              description="Query string for the items to search in the database that ha"
                                              )
                     ):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

