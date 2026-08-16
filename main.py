from fastapi import FastAPI, HTTPException, status


# create app instance
app = FastAPI(
    title="Task API",
    version="1.0"
)

tasks = [
    {"id": 1, "title": "Buy groceries", "done": False},
    {"id": 2, "title": "Read a chapter", "done": True},
    {"id": 3, "title": "Complete assignment", "done": False},
]


#in stage 1 and 0:
@app.get('/', summary="root endpoint")
async def read_root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


@app.get("/health" ,summary="Health check")
def get_health():
    return {
        "status": "ok"
    }

# in stage 2:
@app.get("/tasks", summary="List all tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}", summary="Get a single task by ID")
def get_task_by_id(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
            
    # if the task not found :
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {id} not found"
    )



    
