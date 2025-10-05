from fastapi import FastAPI
from app.posts.router import router as posts_router


app = FastAPI()
app.include_router(posts_router)

