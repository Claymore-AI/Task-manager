from django.urls import path
from task_manager.views import TaskListView, HomeView

app_name = "task_manager"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("/tasks", TaskListView.as_view(), name="task-list")
]