from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("completed", "Completed")],
        default="pending"
    )
    assigned_users = models.ManyToManyField(User, related_name="tasks", blank=True)

    def __str__(self):
        return self.name
