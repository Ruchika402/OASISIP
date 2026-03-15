# Django Tailwind Todo App

A stylish, functional Todo application built with Django and Tailwind CSS. It allows users to track tasks, mark them as completed, and manage their daily workflow with a modern UI.

## Features

- **Add Tasks**: Provide a title and an optional description for your tasks.
- **Visual Status**: Tasks are clearly marked as "Running" (Pending) or "Completed" with distinct colors.
- **One-Click Completion**: Easily mark tasks as done.
- **Deletion**: Remove tasks from your list permanently.
- **Responsive UI**: Built with Tailwind CSS for a clean, mobile-friendly experience.
- **Timestamping**: See how long ago each task was added.

## Prerequisites

- Python 3.8 or higher installed on your system.
- pip (Python package installer).

## Installation

1.  **Clone or create the project files** as provided in the structure.
2.  **Open your terminal** in the project root directory.
3.  **Install Django**:
    bash
    pip install -r requirements.txt

## How to Run

1.  **Prepare the Database**:
    Run the migrations to create the database schema:
    bash
    python manage.py makemigrations tasks
    python manage.py migrate

2.  **Start the Server**:
    bash
    python manage.py runserver

3.  **Access the App**:
    Open your web browser and go to `http://127.0.0.1:8000`.

## Configuration Instructions

- **Port**: By default, it runs on port 8000. You can change it by running `python manage.py runserver 8080`.
- **Database**: Uses SQLite (`db.sqlite3`) by default, requiring no external database setup.

## Project Structure

- `tasks/`: contains the core logic, models for tasks, and URL routing.
- `todo_project/`: configuration files, settings, and main URL entry point.
- `templates/tasks/`: holds the HTML template using Tailwind CSS for the user interface.
- `manage.py`: Django's command-line utility.

## Troubleshooting

- **Migrations error**: If you encounter issues with database tables, delete `db.sqlite3` and the contents of `tasks/migrations/` (except `__init__.py`) and run the migrate commands again.
- **Tailwind not loading**: The app uses the Tailwind CDN, so an active internet connection is required to load the styles correctly.
