from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import User, Task

User = get_user_model()


class UserModelTest(TestCase):
    """Test cases for User model"""
    
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'age': 25,
            'bio': 'Test bio'
        }
    
    def test_create_user(self):
        """Test creating a user"""
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.age, 25)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
    
    def test_user_str_method(self):
        """Test User __str__ method"""
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(str(user), 'testuser')
    
    def test_get_full_display_name(self):
        """Test get_full_display_name method"""
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.get_full_display_name(), 'Test User')
        
        # Test with no first/last name
        user_no_name = User.objects.create_user(
            username='noname',
            email='noname@example.com'
        )
        self.assertEqual(user_no_name.get_full_display_name(), 'noname')
    
    def test_user_email_unique(self):
        """Test that email must be unique"""
        User.objects.create_user(**self.user_data)
        
        with self.assertRaises(Exception):
            User.objects.create_user(
                username='testuser2',
                email='test@example.com',  # Same email
                password='testpass123'
            )


class TaskModelTest(TestCase):
    """Test cases for Task model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.task_data = {
            'title': 'Test Task',
            'description': 'Test task description',
            'created_by': self.user
        }
    
    def test_create_task(self):
        """Test creating a task"""
        task = Task.objects.create(**self.task_data)
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'Test task description')
        self.assertFalse(task.completed)
        self.assertEqual(task.created_by, self.user)
    
    def test_task_str_method(self):
        """Test Task __str__ method"""
        task = Task.objects.create(**self.task_data)
        self.assertEqual(str(task), 'Test Task')
    
    def test_task_ordering(self):
        """Test that tasks are ordered by creation date (newest first)"""
        task1 = Task.objects.create(title='Task 1', created_by=self.user)
        task2 = Task.objects.create(title='Task 2', created_by=self.user)
        
        tasks = Task.objects.all()
        self.assertEqual(tasks[0], task2)  # Newest first
        self.assertEqual(tasks[1], task1)
