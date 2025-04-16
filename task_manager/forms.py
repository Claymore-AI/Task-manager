from django import forms
from django.db.models import QuerySet
from task_manager.models import Task


class TaskForm(forms.ModelForm):
    task_queryset: QuerySet = Task.objects.all()

    task = forms.ModelMultipleChoiceField(
        queryset=task_queryset, widget=forms.CheckboxSelectMultiple, required=False
    )

    class Meta:
        model = Task
        fields = "__all__"