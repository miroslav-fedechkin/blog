from fastapi import FastAPI
from app.posts.router import router as posts_router
from app.comments.router import router as comments_router


app = FastAPI()
app.include_router(posts_router)
app.include_router(comments_router)

