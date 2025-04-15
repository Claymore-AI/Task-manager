from django.contrib import admin
from task_manager.models import Task, Worker, TaskType, Position

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "created_date", "priority", "task_type", "deadline"]
    filter_horizontal = ["assignees"]

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "position"]
    search_fields = ["position__name",]

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    ...

@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    ...


