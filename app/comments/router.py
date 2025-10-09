from fastapi import APIRouter, Depends
from app.comments.schemas import SComment
from typing import Annotated
from app.comments.repository import *

router = APIRouter(
    prefix='/comments',
    tags=['Comments']
)


@router.post('/add')
async def add_comment_to_post(comment: Annotated[SComment, Depends()], post_id: int):
    new_comment = await CommentsRepo.add_comment(comment, post_id)
    return new_comment