from django.contrib import admin
from task_manager.models import Task, Worker, TaskType, Position


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "created_date",
        "priority",
        "task_type",
        "deadline",
        "is_completed",
    ]
    list_filter = ["priority", "task_type", "is_completed"]
    search_fields = ["name", "description"]
    filter_horizontal = ["assignees"]
    ordering = ["-created_date"]


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "first_name", "last_name", "position"]
    list_filter = ["position"]
    search_fields = ["username", "email", "first_name", "last_name", "position__name"]
    ordering = ["username"]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    ordering = ["name"]
