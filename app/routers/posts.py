from fastapi import APIRouter
from ..models import Post
from datetime import datetime
# from app.main import db
from sqlalchemy.orm import Session

db = Session()

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}}
)


@router.get("/")
def post_list():
    posts = db.query(Post).all()
    return posts

#
# @router.post("/")
# async def post_create(db: Session):
#     post = Post(title=title, content=, createAt=datetime.now().replace(microsecond=0))
#     db.add(post)
#     db.commit()
#     db.refresh(post)
#     return post


