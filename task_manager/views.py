from datetime import timezone

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView
from task_manager.models import Task, TaskType, Position, Worker
from django.views import generic
from task_manager.forms import TaskForm, WorkerCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "task_manager/home.html"
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name ="task_manager/task_list.html"
    context_object_name = "task_list"
    paginate_by = 6

    def get_queryset(self):
        return Task.objects.order_by("priority", "deadline")

class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")

class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "task_manager/task_confirm_delete.html"
    success_url = reverse_lazy("task_manager:task-list")

class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")

class SignUpView(CreateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
