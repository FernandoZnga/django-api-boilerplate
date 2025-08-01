from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import override_settings
from django.contrib.auth import get_user_model

from ..models import User, Task

User = get_user_model()


@override_settings(DEBUG=True)
class UITest(StaticLiveServerTestCase):
    """UI tests using Selenium"""
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Set up Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        
        try:
            cls.driver = webdriver.Chrome(options=chrome_options)
            cls.driver.implicitly_wait(10)
        except Exception as e:
            # If Chrome driver is not available, skip UI tests
            cls.driver = None
            print(f"Warning: Chrome driver not available, skipping UI tests: {e}")
    
    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()
        super().tearDownClass()
    
    def setUp(self):
        if not self.driver:
            self.skipTest("Chrome driver not available")
        
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.task = Task.objects.create(
            title='Test Task for UI',
            description='This is a test task for UI testing',
            created_by=self.user
        )
    
    def test_home_page_load(self):
        """Test that home page loads correctly"""
        self.driver.get(f'{self.live_server_url}/')
        
        # Check page title (should be "Home")
        self.assertEqual(self.driver.title, 'Home')
        
        # Check for main heading
        heading = self.driver.find_element(By.TAG_NAME, 'h1')
        self.assertEqual(heading.text, 'Django API Boilerplate')
        
        # Check for stats
        stats_div = self.driver.find_element(By.CLASS_NAME, 'stats')
        self.assertIn('Total Users: 1', stats_div.text)
        self.assertIn('Total Tasks: 1', stats_div.text)
    
    def test_navigation_links(self):
        """Test navigation links work"""
        self.driver.get(f'{self.live_server_url}/')
        
        # Test Home link
        home_link = self.driver.find_element(By.LINK_TEXT, 'Home')
        home_link.click()
        self.assertEqual(self.driver.title, 'Home')
        
        # Test Tasks link
        tasks_link = self.driver.find_element(By.LINK_TEXT, 'Tasks')
        tasks_link.click()
        
        # Wait for page to load and check content
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'h2'))
        )
        heading = self.driver.find_element(By.TAG_NAME, 'h2')
        self.assertEqual(heading.text, 'All Tasks')
    
    def test_tasks_page_display(self):
        """Test tasks page displays tasks correctly"""
        self.driver.get(f'{self.live_server_url}/tasks/')
        
        # Check page has tasks
        task_elements = self.driver.find_elements(By.CLASS_NAME, 'task')
        self.assertEqual(len(task_elements), 1)
        
        # Check task details
        task_element = task_elements[0]
        self.assertIn('Test Task for UI', task_element.text)
        self.assertIn('This is a test task for UI testing', task_element.text)
        self.assertIn('testuser', task_element.text)
        self.assertIn('Pending', task_element.text)
    
    def test_tasks_page_empty_state(self):
        """Test tasks page when no tasks exist"""
        Task.objects.all().delete()
        self.driver.get(f'{self.live_server_url}/tasks/')
        
        # Check for empty message
        empty_message = self.driver.find_element(By.ID, 'no-tasks-message')
        self.assertEqual(empty_message.text, 'No tasks available.')
    
    def test_completed_task_styling(self):
        """Test that completed tasks have different styling"""
        # Create a completed task
        completed_task = Task.objects.create(
            title='Completed Task',
            description='This task is completed',
            completed=True,
            created_by=self.user
        )
        
        self.driver.get(f'{self.live_server_url}/tasks/')
        
        # Find the completed task element
        completed_task_element = self.driver.find_element(
            By.XPATH, f'//div[@data-task-id="{completed_task.id}"]'
        )
        
        # Check it has the completed class
        classes = completed_task_element.get_attribute('class')
        self.assertIn('completed', classes)
        
        # Check status text
        status_element = completed_task_element.find_element(
            By.CLASS_NAME, 'status-completed'
        )
        self.assertEqual(status_element.text, 'Completed')
