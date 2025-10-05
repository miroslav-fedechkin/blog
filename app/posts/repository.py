from sqlalchemy import select
from app.database import async_session_maker
from app.posts.models import Post

class PostsRepo:

    @classmethod
    async def add_post(
        cls,
        post: Post
    ):
        async with async_session_maker() as session:
            new_post = Post(title = post.title, content = post.content)        
            
            session.add(new_post)
            await session.commit()
            await session.refresh(new_post)
            return new_post
        

    @classmethod
    async def get_post(
        cls,
        post_id: int
    ):
        async with async_session_maker() as session:
            query = select(Post).where(Post.id == post_id)
            result = await session.execute(query)
            id = result.scalar_one_or_none()
            return id