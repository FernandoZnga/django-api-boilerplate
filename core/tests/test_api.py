from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Task, User

User = get_user_model()


class APITest(APITestCase):
    """Test cases for API endpoints"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.admin_user = User.objects.create_superuser(
            username="admin", email="admin@example.com", password="adminpass123"
        )
        self.task = Task.objects.create(
            title="Test Task", description="Test description", created_by=self.user
        )

    def test_create_user_api(self):
        """Test creating user via API (public endpoint)"""
        url = reverse("core:api_users")
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpass123",
            "first_name": "New",
            "last_name": "User",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)  # 2 existing + 1 new

    def test_list_users_authenticated(self):
        """Test listing users requires authentication"""
        url = reverse("core:api_users")

        # Unauthenticated request
        response = self.client.get(url)
        self.assertIn(
            response.status_code,
            [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN],
        )

        # Authenticated request
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)  # 2 users total

    def test_get_user_detail(self):
        """Test getting user detail"""
        self.client.force_authenticate(user=self.user)
        url = reverse("core:api_user_detail", kwargs={"pk": self.user.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "testuser")
        self.assertEqual(response.data["email"], "test@example.com")

    def test_create_task_api(self):
        """Test creating task via API"""
        self.client.force_authenticate(user=self.user)
        url = reverse("core:api_tasks")
        data = {
            "title": "New Task",
            "description": "New task description",
            "completed": False,
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)  # 1 existing + 1 new
        new_task = Task.objects.get(title="New Task")
        self.assertEqual(new_task.created_by, self.user)

    def test_list_tasks_authenticated(self):
        """Test listing tasks requires authentication"""
        url = reverse("core:api_tasks")

        # Unauthenticated request
        response = self.client.get(url)
        self.assertIn(
            response.status_code,
            [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN],
        )

        # Authenticated request
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_update_task(self):
        """Test updating a task"""
        self.client.force_authenticate(user=self.user)
        url = reverse("core:api_task_detail", kwargs={"pk": self.task.pk})
        data = {
            "title": "Updated Task",
            "description": "Updated description",
            "completed": True,
        }
        response = self.client.patch(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated Task")
        self.assertTrue(self.task.completed)

    def test_delete_task(self):
        """Test deleting a task"""
        self.client.force_authenticate(user=self.user)
        url = reverse("core:api_task_detail", kwargs={"pk": self.task.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_api_stats(self):
        """Test API stats endpoint"""
        self.client.force_authenticate(user=self.user)
        url = reverse("core:api_stats")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_users"], 2)
        self.assertEqual(response.data["total_tasks"], 1)
        self.assertEqual(response.data["completed_tasks"], 0)
        self.assertEqual(response.data["current_user"], "testuser")
