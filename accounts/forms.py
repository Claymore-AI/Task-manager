from django.contrib.auth.forms import UserCreationForm

from task_manager.models import Worker


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
