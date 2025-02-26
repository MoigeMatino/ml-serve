# from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.routes import router
# from app.db import init_db

# don't need this to run on startup, handled by alembic
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Initialize the database
#     init_db()
#     yield

def create_app() -> FastAPI:
    # app = FastAPI(lifespan=lifespan)
    app = FastAPI()
    app.include_router(router)
    return app

app = create_app()