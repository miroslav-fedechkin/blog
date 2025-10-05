from pydantic import BaseModel
from typing import Optional

class SPost(BaseModel):
    title: str
    content: str

class SResponsePost(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes: True