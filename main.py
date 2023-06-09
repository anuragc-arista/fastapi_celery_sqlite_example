import uvicorn as uvicorn
from fastapi import FastAPI

from config.celery_utils import create_celery
from routers import fibonacci


def create_app() -> FastAPI:
    current_app = FastAPI(title="Asynchronous tasks processing with Celery and sqlite",
                          description="Sample FastAPI Application to demonstrate Event" 
                          "driven architecture with Celery and sqlLite",
                          version="1.0.0", )

    current_app.celery_app = create_celery()
    current_app.include_router(fibonacci.router)
    return current_app


app = create_app()
celery = app.celery_app


if __name__ == "__main__":
    uvicorn.run("main:app", port=5001, reload=True)
