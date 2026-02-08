from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task


# ---------- Model Tests ----------
class TaskModelTest(TestCase):

    def test_task_creation(self):
        task = Task.objects.create(title="Test Task")
        self.assertEqual(task.title, "Test Task")

    def test_default_status(self):
        task = Task.objects.create(title="Default Status Task")
        self.assertEqual(task.status, "Pending")


# ---------- API Tests ----------
class TaskAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = "/api/tasks/"

    def test_create_task(self):
        data = {
            "title": "Buy groceries",
            "status": "Pending"
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_tasks(self):
        Task.objects.create(title="Task 1")
        Task.objects.create(title="Task 2")

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_status(self):
        data = {
            "title": "Invalid Task",
            "status": "Done"   # invalid (only Pending/Completed allowed)
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

