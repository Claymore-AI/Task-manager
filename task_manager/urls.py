from django.urls import path
from task_manager.views import (
    TaskListView,
    HomeView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    SignUpView,
    WorkerListView,
    toggle_task_status,
    WorkerDetailView,
)

app_name = "task_manager"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("tasks/<int:task_id>/toggle/", toggle_task_status, name="toggle-task-status"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
]
