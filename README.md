# Task Manager REST API

A simple and robust RESTful Task Manager API built with Python 3.13 and FastAPI. This project implements standard CRUD operations, Pydantic data validation, dynamic UUID generation, and in-memory storage.

---

## 🚀 Features & API Endpoints

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| `GET` | `/health` | API Health Check | `200 OK` |
| `POST` | `/tasks` | Create a new task | `201 Created` |
| `GET` | `/tasks` | Retrieve all tasks | `200 OK` |
| `GET` | `/tasks/{id}` | Retrieve a specific task by UUID | `200 OK` / `404 Not Found` |
| `PUT` | `/tasks/{id}` | Update an existing task | `200 OK` / `404 Not Found` |
| `DELETE` | `/tasks/{id}` | Delete a task by UUID | `204 No Content` / `404 Not Found` |

---

## 💻 Local Development Setup

```bash
# 1. Clone the repository
git clone [https://github.com/MAHISHARMA-2023A1R078/task-manager-api.git](https://github.com/MAHISHARMA-2023A1R078/task-manager-api.git)
cd task-manager-api

# 2. Set up virtual environment
python -m venv venv
source venv/Scripts/activate  # On Windows Git Bash

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run application locally
uvicorn main:app --reload



# Initialize & Create Feature Branch
git init
git checkout -b feature/task-api-implementation

# Commit changes
git add .
git commit -m "feat: implement FastAPI task manager REST API"

# Add Remotes (GitHub & GitLab)
git remote add origin [https://github.com/MAHISHARMA-2023A1R078/task-manager-api.git](https://github.com/MAHISHARMA-2023A1R078/task-manager-api.git)
git remote add gitlab [https://gitlab.com/mahisharma11a18/task-manager-api.git](https://gitlab.com/mahisharma11a18/task-manager-api.git)

# Push Feature Branch to both remotes
git push origin feature/task-api-implementation
git push gitlab feature/task-api-implementation

# After merging Pull Request (GitHub) / Merge Request (GitLab) online:
git checkout main
git pull origin main