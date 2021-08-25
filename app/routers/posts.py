from fastapi import APIRouter

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}}
)


@router.get("/posts/")
async def post_list():
    return


