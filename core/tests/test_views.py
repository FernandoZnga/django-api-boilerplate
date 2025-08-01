from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from ..models import Task, User

User = get_user_model()


class ViewsTest(TestCase):
    """Test cases for Django views"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.task = Task.objects.create(
            title="Test Task", description="Test description", created_by=self.user
        )

    def test_home_view(self):
        """Test home view"""
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django API Boilerplate")
        self.assertContains(response, "Total Users:</strong> 1")
        self.assertContains(response, "Total Tasks:</strong> 1")

    def test_tasks_list_view(self):
        """Test tasks list view"""
        response = self.client.get(reverse("core:tasks_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")
        self.assertContains(response, "testuser")

    def test_tasks_list_view_empty(self):
        """Test tasks list view when no tasks exist"""
        Task.objects.all().delete()
        response = self.client.get(reverse("core:tasks_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No tasks available")
