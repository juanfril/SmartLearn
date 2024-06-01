import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
  return APIClient()

@pytest.mark.django_db
def test_create_user(api_client):
  data = {
    "username": "newuser",
    "email": "newuser@test.com",
    "password": "password123"
  }
  response = api_client.post('/api/users', data, format='json')
  assert response.status_code == 201
  assert User.objects.count() == 1
  assert User.objects.get(id=response.data['id']).username == 'newuser'

@pytest.mark.django_db
def test_get_user(api_client):
  User.objects.create_user(
    username="testuser",
    email="testuser@test.com",
    password="password123"
  )
  response = api_client.get('/api/users')
  assert response.status_code == 200
  assert "testuser" in response.content.decode()
