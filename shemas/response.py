from pydantic import BaseModel
from typing_extensions import List


from shemas.tasks import STask



class SResponseAllTasks(BaseModel):
    status_code: int
    data: List[STask]



class SResponseAddTask(BaseModel):
    detail: str
    task_id: int
    response_code: int
