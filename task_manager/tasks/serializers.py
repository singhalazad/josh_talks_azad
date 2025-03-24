from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    assigned_users = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, required=False
    )

    class Meta:
        model = Task
        fields = ["id", "name", "description", "created_at", "task_type", "status", "assigned_users"]
