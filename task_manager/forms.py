from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import QuerySet
from task_manager.models import Task, Worker, Position


class TaskForm(forms.ModelForm):
    task_queryset: QuerySet = Task.objects.all()

    task = forms.ModelMultipleChoiceField(
        queryset=task_queryset, widget=forms.CheckboxSelectMultiple, required=False
    )

    class Meta:
        model = Task
        fields = "__all__"

class WorkerCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = ("username", "first_name", "last_name", "position", "password1", "password2")
        labels = {
            "username": "Username",
            "first_name": "First Name",
            "last_name": "Last Name",
            "position": "Position",
            "password1": "Password",
            "password2": "Confirm Password",
        }