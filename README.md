# josh_talks_azad

# Features:

1)Create a new task

2)Assign a task to one or more users

3)Fetch tasks assigned to a specific user

# Prerequisites:

Ensure you have the following installed on your system:

Python (>=3.8)

Django (>=4.0)

Django REST Framework

PostgreSQL or SQLite (default)

Installation & Setup

1️⃣ Clone the Repository

 git clone https://github.com/yourusername/task-management-api.git
 cd task-management-api

2️⃣ Create & Activate Virtual Environment

python -m venv env  # Create virtual environment
source env/bin/activate  # Activate (Linux/macOS)
# On Windows, use: env\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Configure Database ( SQLite)

 we used the default SQLite configuration.

5️⃣ Apply Migrations

python manage.py makemigrations
python manage.py migrate

6️⃣ Create a Superuser

python manage.py createsuperuser

7️⃣ Run the Server

python manage.py runserver

API Endpoints

📌 Create a Task

# http://127.0.0.1:8000/api/tasks/create/

{
    "name": "New Task",
    "description": "This is a sample task",
    "task_type": "Coding",
    "status": "pending"
}

📌 Assign Task to a User

# http://127.0.0.1:8000/api/tasks/{task_id}/assign/

{
    "assigned_users": [1]  
}

📌 Get Tasks Assigned to a User

# http://127.0.0.1:8000/api/tasks/user/{user_id}/

