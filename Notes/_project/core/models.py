from django.db import models


class Note(models.Model):
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    content = models.TextField()
    is_completed = models.BooleanField()
    note = models.ForeignKey("Note", on_delete=models.CASCADE, related_name="tasks")

