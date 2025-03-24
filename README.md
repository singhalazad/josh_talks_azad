# josh_talks_azad


# 1) create tasks API:

# http://127.0.0.1:8000/api/tasks/create/

# payload:  {
                "name": "Test Task",
                "description": "This is a test task",
                "task_type": "Coding",
                "status": "pending"
            }

# 2) assign task to User API:
# http://127.0.0.1:8000/api/tasks/1/assign/
# payload: {
                "assigned_users": [1]
            }

# 3) Fetches all tasks assigned to a particular user API:
# http://127.0.0.1:8000/api/tasks/user/1/

