from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI(
    title="Task Manager REST API using python and Fast API",
    description="In-memory Task Manager REST API built with FastAPI",
    version="1.0.0"
)

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskResponse(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    completed: bool

# In-memory storage
tasks_db: dict[str, dict] ={}

@app.get("/health", status_code=status.HTTP_200_OK, tags=["Health"])
def health_check():
    return {"status": "healthy", "service": "Task Manager API"}

@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED, tags=["Tasks"])
def create_task(task: TaskCreate):
    task_id = str(uuid.uuid4())
    new_task = {"id": task_id, **task.model_dump()}
    tasks_db[task_id] = new_task
    return new_task

@app.get("/tasks", response_model=List[TaskResponse], tags=["Tasks"])
def get_all_tasks():
    return list(tasks_db.values())

@app.get("/tasks/{task_id}", response_model=TaskResponse, tags=["Tasks"])
def get_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail=f"Task with ID '{task_id}' not found")
    return tasks_db[task_id]

@app.put("/tasks/{task_id}", response_model=TaskResponse, tags=["Tasks"])
def update_task(task_id: str, updated_task: TaskCreate):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail=f"Task with ID '{task_id}' not found")
    
    task_data = {"id": task_id, **updated_task.model_dump()}
    tasks_db[task_id] = task_data
    return task_data

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tasks"])
def delete_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail=f"Task with ID '{task_id}' not found")
    del tasks_db[task_id]
    return None