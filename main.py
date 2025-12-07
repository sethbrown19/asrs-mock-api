from fastapi import FastAPI, HTTPException
from typing import Annotated
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI()

tasks_db = {}

class TaskType(str, Enum):
    stow = "stow"
    retrieve = "retrieve"

class Task(BaseModel):
    task_id: str
    type: TaskType
    ndc: str
    quantity: Annotated[int, Field(gt=0)]
    
class TaskResponse(Task):
    status: str

@app.get("/")
def root():
    return {"ok": True}

@app.get("/hello")
def hello():
    return {"message": "hello from ASRS mock API"}

@app.post("/tasks", response_model=TaskResponse, status_code=202)
def create_retrieve_task(task : Task):
    response = TaskResponse(**task.model_dump(), status= "accepted")
    tasks_db[task.task_id] = response
    return response

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]


