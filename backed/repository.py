from sqlalchemy import select, delete

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
                STask.model_validate(dict(id=task.id, name=task.name, description=task.description)) for task in
                task_models
            ]
            return task_schemas

    @classmethod
    async def get_one(cls, task_id: int) -> STask:
        async with new_session() as db:
            task = await db.scalar(
                select(TaskOrm).where(TaskOrm.id == task_id)
            )
            # print(task)
            if not task:
                return STask(id=0, name="Пусто", description="Пусто")
            else:
                return task



    @classmethod
    async def delete_one(cls, task_id: int):
        async with new_session() as db:
            await db.execute(
                delete(TaskOrm).where(TaskOrm.id == task_id)
            )
            await db.commit()
