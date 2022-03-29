from typing import Optional
from pydantic import BaseModel

class Category(BaseModel):
    category_id: str
    category_name: Optional[str]
    category_description: Optional[str]

