from typing import Any
from django.db import models

class Course(models.Model):
    title: str = models.CharField(max_length=255)
    description: str = models.TextField()
    created_at: Any = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
