from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from task_manager.models import Task, TaskType, Position, Worker


class HomeView(TemplateView):
    template_name = "task_manager/home.html"
class TaskListView(ListView):
    model = Task
    template_name ="task_manager/task_list.html"
    context_object_name = "task_list"
    paginate_by = 6

    def get_queryset(self):
        return Task.objects.order_by("priority", "deadline")
