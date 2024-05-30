import pytest
from rest_framework.test import APIClient
from courses.models import Course
from courses.serializers import CourseSerializer

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def course():
    return Course.objects.create(
        title="Test Course",
        description="Test Description"
    )

@pytest.mark.django_db
def test_course_creation(course):
    assert course.title == "Test Course"
    assert course.description == "Test Description"
    assert course.created_at is not None

@pytest.mark.django_db
def test_get_courses(api_client, course):
    response = api_client.get('/api/courses/')
    assert response.status_code == 200
    assert "Test Course" in response.content.decode()

@pytest.mark.django_db
def test_get_single_course(api_client, course):
    response = api_client.get(f'/api/courses/{course.id}/')
    assert response.status_code == 200
    assert "Test Course" in response.content.decode()

@pytest.mark.django_db
def test_create_course(api_client):
    data = {"title": "New Course", "description": "New Description"}
    response = api_client.post('/api/courses/', data, format='json')
    assert response.status_code == 201
    assert Course.objects.count() == 1
    assert Course.objects.get(id=response.data['id']).title == 'New Course'

@pytest.mark.django_db
def test_serializer_fields(course):
    serializer = CourseSerializer(instance=course)
    data = serializer.data
    assert set(data.keys()) == {'id', 'title', 'description', 'created_at'}

@pytest.mark.django_db
def test_serializer_title_content(course):
    serializer = CourseSerializer(instance=course)
    data = serializer.data
    assert data['title'] == course.title
