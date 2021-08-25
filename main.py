from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/posts/{post_id}")
def read_post(post_id: int, q: Optional[str] = None):
    return {"post_id": post_id, "q": q}

@app.put("/posts/{post_id}")
def update_post(post_id: int, post: Post):
    return {"post_title": post.title, "post_content": post.content}

@app.post("/posts/")

