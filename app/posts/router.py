from typing import Annotated
from fastapi import APIRouter, Depends
from app.posts.repository import *
from app.posts.schemas import *

router = APIRouter(
    prefix='/posts',
    tags=['Posts']

)


@router.post('/add', response_model = SResponsePost)
async def add_post(post: Annotated[SPost, Depends()]):
    new_post = await PostsRepo.add_post(post)
    return new_post

@router.get('/get', response_model = SResponsePost)
async def get_post_by_id(post_id: int):
    current_post = await PostsRepo.get_post(post_id)
    return current_post

@router.get('/get_all', response_model=SResponsePost)
async def get_posts():
    posts = await PostsRepo.get_all_posts()
    return posts

@router.delete('/delete')
async def delete_post(post_id: int):
    deleted_post = await PostsRepo.delete_post(post_id)
    return {'status':'success'}