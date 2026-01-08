# Django ToDo App – Full CRUD + Dockerized

A beautiful, responsive ToDo application built with Django featuring full Create, Read, Update, Delete operations and toggle completed status.

## Features
- Add / Edit / Delete / List ToDos
- Toggle completed status
- Clean UI with Bootstrap 5
- Success messages using Django messages framework
- Fully Dockerized with Dockerfile & docker-compose
- Uses SQLite (default)

## Screenshots

| Home Page                  | Add Todo                   | Edit Todo                  |
|----------------------------|----------------------------|----------------------------|
| ![Home](screenshots/home.png) | ![Add](screenshots/add.png) | ![Edit](screenshots/edit.png) |

## Tech Stack
- Django 5.x
- Bootstrap 5
- SQLite
- Docker & Docker Compose

## How to Run Locally (Without Docker)

```bash
git clone https://github.com/Aravind-Babu31/django-todo-crud-app.git
cd django-todo-crud-app
python -m venv venv
venv\Scripts\activate    # On Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver



# CI/CD working! 🚀
