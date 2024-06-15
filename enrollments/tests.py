import pytest
from django.contrib.auth.models import User
from courses.models import Course
from enrollments.models import Enrollment
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def course():
    return Course.objects.create(title="Test Course", description="Test Description")

@pytest.fixture
def user():
    return User.objects.create_user(username="testuser", email="testuser@example.com", password="password123")

@pytest.mark.django_db
def test_create_enrollment(api_client, course, user):
    api_client.login(username='testuser', password='password123')
    data = {"user": user.id, "course": course.id}
    response = api_client.post('/api/enrollments/', data, format='json')
    assert response.status_code == 201
    assert Enrollment.objects.count() == 1
    assert Enrollment.objects.get(id=response.data['id']).user == user

@pytest.mark.django_db
def test_get_enrollments(api_client, course, user):
    Enrollment.objects.create(user=user, course=course)
    api_client.login(username='testuser', password='password123')
    response = api_client.get('/api/enrollments/')
    assert response.status_code == 200
    content = response.json()
    assert len(content) == 1
    assert content[0]['user'] == user.id
    assert content[0]['course'] == course.id
