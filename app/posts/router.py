from fastapi import APIRouter

router = APIRouter(
    prefix='/posts',
    tags=['Posts']

)


@router.post
async def add_post():
    pass