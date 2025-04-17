from django.test import TestCase
from django.utils import timezone
from task_manager.models import Task, TaskType, Worker, Position


class ModelsTestCase(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Bug")
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(
            username="testuser", password="password123", position=self.position
        )

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), "Bug")

    def test_position_str(self):
        self.assertEqual(str(self.position), "Developer")

    def test_worker_creation(self):
        self.assertEqual(self.worker.username, "testuser")
        self.assertEqual(self.worker.position.name, "Developer")

    def test_task_creation_and_str(self):
        task = Task.objects.create(
            name="Fix login",
            description="Fix login page bug",
            deadline=timezone.now() + timezone.timedelta(days=3),
            task_type=self.task_type,
            priority=Task.PriorityChoices.URGENT,
        )
        task.assignees.add(self.worker)
        self.assertEqual(str(task), "Fix login")
        self.assertEqual(task.assignees.count(), 1)
        self.assertIn(self.worker, task.assignees.all())
