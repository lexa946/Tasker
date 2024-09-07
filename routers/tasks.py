from typing import Annotated

from fastapi import APIRouter, Depends, Path
from starlette import status

from backed.repository import TaskRepository
from shemas.tasks import STaskAdd, STask
from shemas.response import SResponseAllTasks, SResponseAddTask

router = APIRouter(prefix='/tasks', tags=['Task'])


@router.get('/')
async def all_tasks() -> SResponseAllTasks:
    tasks_orm = await TaskRepository.get_all()
    return SResponseAllTasks(
        status_code=status.HTTP_200_OK,
        data=tasks_orm,
    )


@router.get('/{task_id}')
async def get_task(task_id: Annotated[int, Path(ge=1)]) -> STask:
    return await TaskRepository.get_one(task_id)



@router.delete('/{task_id}')
async def delete_task(task_id: Annotated[int, Path(ge=1)]):
    await TaskRepository.delete_one(task_id)



@router.post('/')
async def add_task(add_task: Annotated[STaskAdd, Depends()]) -> SResponseAddTask:
    task_id = await TaskRepository.add_one(add_task)
    return {
        'statues_code': status.HTTP_201_CREATED,
        'detail': 'Task add successful!',
        'task_id': task_id
    }
