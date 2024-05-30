from django.test import TestCase
from rest_framework.test import APIClient

from courses.models import Course

class CourseModelTest(TestCase):
  def setUp(self):
    self.course = Course.objects.create(
      title="Test Course",
      description="Test Description"
    )

  def test_course_creation(self):
    self.assertEqual(self.course.title, "Test Course")

class CourseAPITest(TestCase):
  def setup(self):
    self.client = APIClient()
    self.course = Course.objects.create(
      title="Test Course",
      description="Test Description"
    )

  def test_get_courses(self):
    response = self.client.get('/api/courses/')
    self.assertEqual(response.status_code, 200)
