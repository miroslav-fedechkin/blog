from pydantic import BaseModel

class SComment(BaseModel):
    text: str


class SResponseComment(BaseModel):
    id: int
    post_id: int
    text: int

    class Config:
        from_attributes: True