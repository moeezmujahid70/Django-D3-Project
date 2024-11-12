# DjangoD3Project

This project demonstrates how to:
	•	Render a sample D3 chart upon login.
	•	Provide chart data via a protected REST API.
	•	Use JWT for authentication.


[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT


## Prerequisites

	•	Python (3.10+)
	•	Node.js (for frontend dependencies)
	•	PostgreSQL (for the database)
	•	Virtual Environment: pyenv and pyenv-virtualenv


## Getting Started

Follow these steps to get the project running in development mode.

### Create and Activate a Virtual Environment
    
    pyenv virtualenv 3.10.9 d3project_env
    pyenv activate d3project_env
    
### Install Backend Dependencies
    pip install -r requirements/local.txt

### Install Frontend Dependencies
        npm install

### DataBase SetUp
        CREATE DATABASE d3project_db;
        CREATE USER your_user WITH PASSWORD 'your_password';
        GRANT ALL PRIVILEGES ON DATABASE d3project_db TO your_user;

### Run Migrations:
    python manage.py migrate

## Run the Development Server
    $ python manage.py runserver

Access the project at http://127.0.0.1:8000/.


## Settings

Moved to [settings](https://cookiecutter-django.readthedocs.io/en/latest/1-getting-started/settings.html).


## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy d3project
