from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Laboratory Work 8 API")


class TaskCreate(BaseModel):
    title: str


tasks = []
next_id = 1


@app.get("/")
def root():
    return {"message": "Laboratory work 8"}


@app.post("/tasks")
def create_task(task: TaskCreate):
    global next_id

    task_data = {
        "id": next_id,
        "title": task.title,
    }

    tasks.append(task_data)
    next_id += 1

    return task_data


@app.get("/tasks")
def get_tasks():
    return tasks
