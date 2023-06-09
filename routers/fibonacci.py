from celery import group
from fastapi import APIRouter
from starlette.responses import JSONResponse

#from api import universities
from celery_tasks.tasks import computeFib
from config.celery_utils import get_task_info
from schemas.schemas import Input

router = APIRouter(prefix='/fibonacci', tags=['Fibonacci'], responses={404: {"description": "Not found"}})

@router.post("/async")
async def get_fibonacci(input: Input):
    """
         compute fibonacci asynchronously 
    """
    task = computeFib.apply_async(args=[input.input])
    return JSONResponse({"task_id": task.id})


@router.get("/task/{task_id}")
async def get_task_status(task_id: str) -> dict:
    """
    Return the status of the submitted Task
    """
    return get_task_info(task_id)


