from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, DetailView
from task_manager.models import Task, TaskType, Position, Worker
from django.views import generic
from task_manager.forms import TaskForm, WorkerCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = "task_manager/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            tasks = Task.objects.filter(assignees=self.request.user)
            context["total_tasks"] = tasks.count()
            context["completed_tasks"] = tasks.filter(is_completed=True).count()
            context["pending_tasks"] = tasks.filter(is_completed=False).count()
        return context

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_manager/task_list.html"
    context_object_name = "task_list"
    paginate_by = 6

    def get_queryset(self):
        queryset = Task.objects.order_by("is_completed", "priority", "deadline")
        search_query = self.request.GET.get("search", "")
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset


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
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class WorkerListView(LoginRequiredMixin, ListView):
    model = Worker
    template_name = "task_manager/worker_list.html"
    context_object_name = "worker_list"
    paginate_by = 10


def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("task_manager:task-list")


class WorkerDetailView(DetailView):
    model = Worker
    template_name = "task_manager/worker_detail.html"
    context_object_name = "worker"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        worker = self.get_object()
        context["completed_tasks"] = worker.tasks.filter(is_completed=True)
        context["incomplete_tasks"] = worker.tasks.filter(is_completed=False)
        return context
