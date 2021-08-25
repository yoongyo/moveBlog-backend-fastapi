import uvicorn
from app.common.config import conf
from fastapi import FastAPI



db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))


def create_app():
    c = conf()
    app = FastAPI()

    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

