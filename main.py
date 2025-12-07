from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum


app = FastAPI()



class TaskType(str, Enum):
    stow = "stow"
    retrieve = "retrieve"

class Task(BaseModel):
    task_id: str
    type: TaskType
    ndc: str
    quantity: int
    
class TaskResponse(Task):
    status: str

@app.get("/")
def root():
    return {"ok": True}

@app.get("/hello")
def hello():
    return {"message": "hello from ASRS mock API"}

@app.post("/tasks", response_model=TaskResponse, status_code=202)
def create_retrieve_task(task : Task, ):
    return {
        **task.model_dump(),
        "status": "accepted"
    }
