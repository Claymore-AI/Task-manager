from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from core import settings


class TaskType(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Task(models.Model):
    class PriorityChoices(models.TextChoices):
        URGENT = "URGENT", _("Urgent")
        HIGH = "HIGH", _("High")
        MIDDLE = "MIDDLE", _("Middle")
        EAZY = "EAZY", _("EAZY")

    name = models.CharField(max_length=120)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10, choices=PriorityChoices, default=PriorityChoices.MIDDLE
    )

    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="tasks")

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="workers",
    )
    email = models.EmailField(unique=True)
