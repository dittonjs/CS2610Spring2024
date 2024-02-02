from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)