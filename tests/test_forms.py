from django.test import TestCase

from accounts.forms import WorkerCreationForm
from task_manager.forms import TaskForm
from task_manager.models import Task, Worker, Position, TaskType
from django.utils import timezone
from datetime import timedelta


class WorkerCreationFormTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")

    def test_worker_creation_form_valid(self):
        form_data = {
            "username": "john_doe",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "position": self.position.pk,
            "password1": "supersecure123",
            "password2": "supersecure123",
        }
        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_worker_creation_form_invalid_password(self):
        form_data = {
            "username": "john_doe",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "position": self.position.pk,
            "password1": "pass123",
            "password2": "differentpass123",
        }
        form = WorkerCreationForm(data=form_data)
        self.assertFalse(form.is_valid())


class TaskFormTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="QA")
        self.worker = Worker.objects.create_user(
            username="alice", password="testpass123", position=self.position
        )
        self.task_type = TaskType.objects.create(name="Bug")

    def test_task_form_valid(self):
        future_date = timezone.now() + timedelta(days=2)
        form_data = {
            "name": "Fix bug",
            "description": "Fix login bug",
            "deadline": future_date.strftime("%Y-%m-%dT%H:%M"),
            "priority": Task.PriorityChoices.HIGH,
            "task_type": self.task_type.pk,
            "assignees": [self.worker.pk],
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid_without_name(self):
        future_date = timezone.now() + timedelta(days=2)
        form_data = {
            "name": "",
            "description": "Description",
            "deadline": future_date.strftime("%Y-%m-%dT%H:%M"),
            "priority": Task.PriorityChoices.EAZY,
            "task_type": self.task_type.pk,
            "assignees": [self.worker.pk],
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
