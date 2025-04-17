# Task-manager

Task Manager is a simple web application for task management built with Django. It allows users to create, modify, and delete tasks, enabling efficient work management.

## Features

- User registration.
- User login and logout.
- Create, edit, and delete tasks.
- Interface for viewing tasks.

## Technologies

- **Python**: primary programming language.
- **Django**: web framework for the application.
- **Bootstrap**: for styling the user interface.
- **SQLite**: default database.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Claymore-AI/Task-manager.git
   
2. Create and activate a virtual environment:
   ```bash
      python -m venv venv
      source venv/bin/activate  # for Linux/MacOS
      venv\Scripts\activate     # for Windows
3. Install dependencies: You can install dependencies using requirements.txt:
    ```bash
   pip install -r requirements.txt
4. Run database migrations:
   ```bash
   python manage.py migrate
5. Load initial data (recommended for first launch):
   ```bash
   python manage.py loaddata data.json
6. Start the server:
   ```bash
   python manage.py runserver
7. Open your browser and go to http://127.0.0.1:8000/

Usage
To get started, register or log in to the application.

After that, you can create, edit, and delete tasks in your personal dashboard.

## Database Diagram!
[task_manager.drawio](task_manager.drawio)

## Planned Features

## Planned Features

- Sort tasks by type.
- Google authentication.
- Add tags to tasks (many-to-many).
- Support for Projects and Teams.

This project will continue to evolve with regular improvements and new features.