from django.urls import path
from task_manager.views import (
    TaskListView,
    HomeView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    WorkerListView,
    WorkerDetailView,
    ToggleTaskStatusView,
)

app_name = "task_manager"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path(
        "tasks/<int:task_id>/toggle/",
        ToggleTaskStatusView.as_view(),
        name="toggle-task-status",
    ),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
]
