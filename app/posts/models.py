from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Post(Base):
    __tablename__='posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    
    
    comments = relationship('Comment', back_populates='post')
    

