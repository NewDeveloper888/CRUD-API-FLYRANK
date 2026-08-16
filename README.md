# In-Memory CRUD Task API (FastAPI)

A lightweight in-memory REST API built using Python and FastAPI for managing tasks. This project demonstrates foundational backend concepts including CRUD operations, input validation, proper HTTP status codes, error handling, interactive API documentation, and Git version control.

---

##  API Documentation (Swagger UI)

FastAPI automatically generates interactive OpenAPI documentation.

![Swagger UI Preview](screenshots/swagger.png)

Access the live interactive documentation locally at:
* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **ReDoc:** `http://127.0.0.1:8000/redoc`

---

##  Tech Stack

* **Language:** Python 3.10+
* **Framework:** FastAPI
* **Server:** Uvicorn
* **Data Validation:** Pydantic

---

##  Getting Started

### 1. Clone the Repository
```bash
git clone <YOUR_GITHUB_REPO_URL>
cd <REPO_FOLDER_NAME>
```

### 2. Create and Activate Virtual Environment
```bash
# Create environment
python -m venv venv

# Activate (Windows PowerShell):
.\venv\Scripts\activate

# Activate (Linux / macOS):
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Server
```bash
uvicorn main:app --reload --port 8000
```
The server will start at `http://127.0.0.1:8000`.

---

##  API Endpoints

| Method | Endpoint | Description | Status Codes |
| :--- | :--- | :--- | :--- |
| **GET** | `/` | API metadata and root discovery | `200 OK` |
| **GET** | `/health` | Server health check | `200 OK` |
| **GET** | `/tasks` | List all tasks | `200 OK` |
| **GET** | `/tasks/{id}` | Retrieve a specific task by ID | `200 OK`, `404 Not Found` |
| **POST** | `/tasks` | Create a new task | `201 Created`, `400 Bad Request` |
| **PUT** | `/tasks/{id}` | Update an existing task's title or status | `200 OK`, `400 Bad Request`, `404 Not Found` |
| **DELETE** | `/tasks/{id}` | Delete a task | `204 No Content`, `404 Not Found` |

---

##  Testing with cURL

> **Note for Windows PowerShell:** Use `curl.exe` instead of `curl` to view complete HTTP headers.

### 1. Root & Health Check
```bash
curl -i [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
curl -i [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)
```

### 2. Read All Tasks
```bash
curl -i [http://127.0.0.1:8000/tasks](http://127.0.0.1:8000/tasks)
```

### 3. Read Single Task (Success & 404)
```bash
curl -i [http://127.0.0.1:8000/tasks/1](http://127.0.0.1:8000/tasks/1)
curl -i [http://127.0.0.1:8000/tasks/99](http://127.0.0.1:8000/tasks/99)
```

### 4. Create Task (Success & Validation Error)
```bash
# Valid task creation
curl -i -X POST [http://127.0.0.1:8000/tasks](http://127.0.0.1:8000/tasks) \
  -H "Content-Type: application/json" \
  -d '{"title": "Complete Stage 6"}'

# Empty title (Returns 400 Bad Request)
curl -i -X POST [http://127.0.0.1:8000/tasks](http://127.0.0.1:8000/tasks) \
  -H "Content-Type: application/json" \
  -d '{"title": "   "}'
```

### 5. Update Task
```bash
curl -i -X PUT [http://127.0.0.1:8000/tasks/1](http://127.0.0.1:8000/tasks/1) \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy oat milk", "done": true}'
```

### 6. Delete Task (Success & 404)
```bash
curl -i -X DELETE [http://127.0.0.1:8000/tasks/1](http://127.0.0.1:8000/tasks/1)
curl -i -X DELETE [http://127.0.0.1:8000/tasks/99](http://127.0.0.1:8000/tasks/99)
```