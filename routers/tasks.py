from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from backed.repository import TaskRepository
from shemas.tasks import STaskAdd
from shemas.response import SResponseAllTasks, SResponseAddTask

router = APIRouter(prefix='/tasks', tags=['Task'])




@router.get('/')
async def all_tasks() -> SResponseAllTasks:
    tasks_orm = await TaskRepository.get_all()
    return SResponseAllTasks(
        status_code=status.HTTP_200_OK,
        data=tasks_orm,
    )


@router.post('/')
async def add_task(add_task: Annotated[STaskAdd, Depends()]) -> SResponseAddTask:
    task_id = await TaskRepository.add_one(add_task)
    return SResponseAddTask(
        status_code=status.HTTP_201_CREATED,
        detail='Task add successful!',
        task_id=task_id,
    )
