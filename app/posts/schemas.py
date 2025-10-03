from pydantic import BaseModel
from typing import Optional

class SPost(BaseModel):
    id: int
    title: str
    content: str