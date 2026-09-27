from fastapi import FastAPI

# Initialize our web application
app = FastAPI(title="Task Tracker API")

# A starter in-memory database of tasks
tasks = [
    {"id": 1, "title": "Learn Git basics", "done": True},
    {"id": 2, "title": "Push project to GitHub", "done": True},
    {"id": 3, "title": "Run API inside Docker container", "done": False},
]

# Route 1: A welcome/health check endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Task API! Visit /docs to test it interactively."}

# Route 2: Get all tasks
@app.get("/tasks")
def get_all_tasks():
    return {"total": len(tasks), "tasks": tasks}

# Route 3: Add a new task
@app.post("/tasks")
def add_task(title: str):
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }
    tasks.append(new_task)
    return {"message": "Task added successfully!", "task": new_task}