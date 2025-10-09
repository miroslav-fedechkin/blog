from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship


class Comment(Base):
    __tablename__='comments'

    id = Column(Integer, primary_key=True)
    text = Column(String)

    post_id = Column(Integer, ForeignKey('posts.id'))
    posts = relationship('Post', back_populates='comments')
    