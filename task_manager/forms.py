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
