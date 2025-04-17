from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import QuerySet
from django.forms import DateTimeInput
from task_manager.models import Task, Worker, Position


class TaskForm(forms.ModelForm):
    task_queryset = Task.objects.all()

    deadline = forms.DateTimeField(
        widget=DateTimeInput(attrs={"type": "datetime-local"}), required=True
    )

    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "deadline",
            "priority",
            "task_type",
            "assignees",
        ]
        widgets = {
            "assignees": forms.CheckboxSelectMultiple,
            "deadline": DateTimeInput(attrs={"type": "datetime-local"}),
        }


class WorkerCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "position",
            "password1",
            "password2",
        )
        labels = {
            "username": "Username",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "position": "Position",
            "password1": "Password",
            "password2": "Confirm Password",
        }
