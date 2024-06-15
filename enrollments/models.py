from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class Enrollment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  progress = models.IntegerField(default=0)
  enrolled_at = models.DateTimeField(auto_now_add=True)
