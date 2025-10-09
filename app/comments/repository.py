from sqlalchemy import select
from app.database import async_session_maker
from app.comments.models import Comment

class CommentsRepo:

    @classmethod
    async def add_comment(
        cls,
        comment: Comment,
        post_id: int
    ):
        async with async_session_maker() as session:
            new_comment = Comment(text = comment.text, post_id = post_id)

            session.add(new_comment)
            await session.commit()
            await session.refresh(new_comment)
            return new_comment
        

    @classmethod
    async def get_comment_by_id(
        cls,
        comment_id: int
    ):
        async with async_session_maker() as session:
            query = select(Comment).where(Comment.id == comment_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()