from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer

class CreateTaskView(generics.CreateAPIView):
    """API to create a new task"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class AssignTaskView(APIView):
    """API to assign a task to one or multiple users"""

    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        user_ids = request.data.get("assigned_users", [])
        users = User.objects.filter(id__in=user_ids)

        if not users.exists():
            return Response({"error": "Invalid user IDs"}, status=status.HTTP_400_BAD_REQUEST)

        task.assigned_users.set(users)
        return Response({"message": "Task assigned successfully"}, status=status.HTTP_200_OK)

class GetTasksByUserView(generics.ListAPIView):
    """API to get tasks assigned to a specific user"""
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Task.objects.filter(assigned_users__id=user_id)
