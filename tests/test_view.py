from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from task_manager.models import Worker, TaskType, Task, Position


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.position = Position.objects.create(name="QA")
        self.user = Worker.objects.create_user(
            username="testuser", password="password123", position=self.position
        )
        self.task_type = TaskType.objects.create(name="Bug")
        self.task = Task.objects.create(
            name="Fix error",
            description="Fix critical error",
            deadline=timezone.now() + timezone.timedelta(days=2),
            task_type=self.task_type,
            priority=Task.PriorityChoices.URGENT,
        )
        self.task.assignees.add(self.user)

    def test_home_view(self):
        response = self.client.get(reverse("task_manager:home"))
        self.assertEqual(response.status_code, 200)

    def test_task_list_view_requires_login(self):
        response = self.client.get(reverse("task_manager:task-list"))
        self.assertNotEqual(response.status_code, 200)  # Redirects to login

    def test_task_list_view_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("task_manager:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fix error")

    def test_worker_list_view(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("task_manager:worker-list"))
        self.assertContains(response, "testuser")

    def test_worker_detail_view(self):
        self.client.login(username="testuser", password="password123")
        url = reverse("task_manager:worker-detail", args=[self.user.pk])
        response = self.client.get(url)
        self.assertContains(response, "Fix error")

    def test_toggle_task_status(self):
        self.client.login(username="testuser", password="password123")
        self.assertFalse(self.task.is_completed)
        toggle_url = reverse("task_manager:toggle-task-status", args=[self.task.pk])
        response = self.client.post(toggle_url)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_completed)
        self.assertEqual(response.status_code, 302)  # Redirect

    def test_create_view_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post(
            reverse("task_manager:task-create"),
            {
                "name": "New Task",
                "description": "New task description",
                "deadline": (timezone.now() + timezone.timedelta(days=5)).strftime(
                    "%Y-%m-%dT%H:%M"
                ),
                "task_type": self.task_type.id,
                "priority": Task.PriorityChoices.HIGH,
                "assignees": [self.user.id],
            },
        )
        self.assertEqual(Task.objects.count(), 2)
        self.assertRedirects(response, reverse("task_manager:task-list"))

    def test_update_view(self):
        self.client.login(username="testuser", password="password123")
        url = reverse("task_manager:task-update", args=[self.task.id])
        response = self.client.post(
            url,
            {
                "name": "Updated Task",
                "description": "Updated description",
                "deadline": (timezone.now() + timezone.timedelta(days=2)).strftime(
                    "%Y-%m-%dT%H:%M"
                ),
                "task_type": self.task_type.id,
                "priority": Task.PriorityChoices.URGENT,
                "assignees": [self.user.id],
            },
        )
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, "Updated Task")
        self.assertRedirects(response, reverse("task_manager:task-list"))

    def test_delete_view(self):
        self.client.login(username="testuser", password="password123")
        url = reverse("task_manager:task-delete", args=[self.task.id])
        response = self.client.post(url)
        self.assertEqual(Task.objects.count(), 0)
        self.assertRedirects(response, reverse("task_manager:task-list"))
