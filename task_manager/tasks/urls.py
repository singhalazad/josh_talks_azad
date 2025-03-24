from django.urls import path
from .views import CreateTaskView, AssignTaskView, GetTasksByUserView

urlpatterns = [
    path("tasks/create/", CreateTaskView.as_view(), name="create_task"),
    path("tasks/<int:task_id>/assign/", AssignTaskView.as_view(), name="assign_task"),
    path("tasks/user/<int:user_id>/", GetTasksByUserView.as_view(), name="get_tasks_by_user"),
]
