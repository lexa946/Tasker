from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from routers import tasks, front

from backed.repository import TaskRepository




app = FastAPI()

app.include_router(tasks.router)
app.include_router(front.router)








app.mount('/static', StaticFiles(directory='static'), 'static')


@app.on_event("startup")
async def startup_event():
    from config import MAX_COUNT_TASKS
    MAX_COUNT_TASKS -= await TaskRepository.get_count_tasks()


