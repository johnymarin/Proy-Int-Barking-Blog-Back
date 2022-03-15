from typing import Optional

from fastapi import APIRouter, Path, Query

api_router = APIRouter()

@api_router.get("/items/{item_id}")
async def read_items(
        item_id: int = Path(..., title="The ID of the item to get"),
        q: Optional[str] = Query(None, alias="item_query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

#ToDo: continue number validations