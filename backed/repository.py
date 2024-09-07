from sqlalchemy import select

from backed.db import new_session
from models.tasks import TaskOrm
from shemas.tasks import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, task: STaskAdd) -> int:
        async with new_session() as db:
            task = TaskOrm(**task.model_dump())
            db.add(task)
            await db.flush()
            await db.commit()
            return task.id

    @classmethod
    async def get_all(cls) -> list[STask]:
        async with new_session() as db:
            query = select(TaskOrm)
            result = await db.execute(query)
            task_models = result.scalars().all()
            task_schemas = [
                STask.model_validate(dict(id=task.id, name=task.name, description=task.description)) for task in task_models
            ]
            print(task_schemas)
            return task_schemas

