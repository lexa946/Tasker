from typing import Annotated

from fastapi import APIRouter, Request, Form, Path, HTTPException
from fastapi.templating import Jinja2Templates

from routers.tasks import all_tasks, add_task, get_task
from shemas.tasks import STaskAdd


router = APIRouter(prefix='/tasker', tags=['Main'])
templates = Jinja2Templates(directory="templates")


@router.get('/')
async def index(request: Request):
    tasks = await all_tasks()
    return templates.TemplateResponse(r"index.html", {
        "request": request, "tasks": tasks.data
    })


@router.post('/')
async def add_task_front(request: Request, task: Annotated[STaskAdd, Form()]):

    if not task.name:
        return templates.TemplateResponse(r"index.html", {
        "request": request, "exception": "Поле Название обязательно к заполнению!"
    })

    await add_task(add_task=task)


    return await index(request)


@router.get('/task/{task_id}')
async def get_task_detail(request: Request, task_id: Annotated[int, Path(ge=1)]):
    task = await get_task(task_id)
    return templates.TemplateResponse(r"index.html", {
        "request": request, "task": task
    })