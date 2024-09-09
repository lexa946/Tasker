from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from routers import tasks, front


app = FastAPI()

app.include_router(tasks.router)
app.include_router(front.router)


app.mount('/static/tasker', StaticFiles(directory='tasker/static'), 'tasker_static')



