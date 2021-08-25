from sqlalchemy.orm import Session
from ..models import Post


def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def create_post(db: Session):
    pass