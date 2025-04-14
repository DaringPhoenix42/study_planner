# 📖 Study Planner

Study Planner is a **Django-based web application** designed to help students organize their academic life by managing notes, homework, to-dos, and resources in one unified platform. This project emphasizes ease of use, a clean and intuitive interface, and scalability for future enhancements.

---

# Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Project Structure](#project-structure)
- [Configuration & Environment Variables](#configuration--environment-variables)
- [User Authentication](#user-authentication)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features

- **User Authentication**: Secure registration, login, and logout processes.
- **Notes Management**: Create, edit, and delete personal study notes.
- **Homework Tracker**: Manage assignments with due dates and status updates.
- **To-Do List**: Keep track of daily tasks and priorities.
- **Educational Resources**: Save and organize educational links including books, YouTube videos, and Wikipedia articles.
- **User Profile**: Update personal details and upload an avatar.
- **Responsive Design**: Optimized for both desktop and mobile devices.

---

## Tech Stack

- **Backend**: [Django](https://www.djangoproject.com/) (Python)
- **Frontend**: HTML, CSS, JavaScript, [Bootstrap](https://getbootstrap.com/)
- **Database**: SQLite (default), with support for PostgreSQL or MySQL in production
- **Icons**: [FontAwesome](https://fontawesome.com/)
- **Deployment (Optional)**: Docker, AWS, Heroku

---

## Installation & Setup

### 1. Clone the Repository
Clone the repository from GitHub to your local machine:
```bash
git clone https://github.com/YourUsername/study_planner.git
cd study_planner
```

### 2. Create & Activate a Virtual Environment
It is recommended to use a virtual environment to manage your project's dependencies.
- **On Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
Install the required packages using the provided `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root to manage your environment-specific settings (such as secret keys, debug settings, and database configurations). For example:
```dotenv
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
STUDY_PLANNER_ENV=development
```
> **Note:** Make sure to add `.env` to your `.gitignore` to prevent sensitive data from being committed.

### 5. Run Migrations
Apply database migrations to set up your database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser
Set up an admin account to manage the application:
```bash
python manage.py createsuperuser
```
Then, you can log in to the admin dashboard at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

### 7. Start the Development Server
Launch the application locally:
```bash
python manage.py runserver
```
Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to start using the app.

---

## Project Structure

Below is a brief overview of the project's directory structure:

```
study_planner/
├── study_planner/      # Django project configuration (settings, URLs, WSGI, etc.)
├── users/              # User authentication & profile management
├── notes/              # Notes creation, editing, and management
├── homework/           # Homework tracking and assignment management
├── todo/               # To-do list functionality for daily tasks
├── resources/          # Educational resources (books, videos, links, etc.)
├── templates/          # HTML templates for rendering frontend views
├── static/             # Static files (CSS, JavaScript, images)
├── manage.py           # Django management script
└── requirements.txt    # Python package dependencies
```

---

## Configuration & Environment Variables

For flexible configuration, the application uses environment variables. You can set these in a `.env` file. Some key variables include:

- **DEBUG**: Set to `True` for development.
- **SECRET_KEY**: Your Django secret key.
- **DATABASE_URL**: Database connection string (e.g., for SQLite, PostgreSQL, or MySQL).
- **STUDY_PLANNER_ENV**: Custom environment variable for your project settings.

---

## User Authentication

User authentication is integrated using Django’s built-in authentication system. To manage users:
- **Sign Up:** Users can register an account.
- **Login/Logout:** Secure login and logout functionality.
- **Profile Management:** Users can update personal information and upload a profile image.

---

## Deployment

### Optional: Docker Deployment
If you choose to deploy using Docker, include a `Dockerfile` and a `docker-compose.yml` in your project. A sample `Dockerfile` might look like:
```dockerfile
FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

CMD ["gunicorn", "study_planner.wsgi:application", "--bind", "0.0.0.0:8000"]
```
For production deployments on AWS or Heroku, follow the respective platform guidelines for Django applications.

---

## Contributing

Contributions are welcome! If you'd like to contribute:

1. **Fork** the repository.
2. **Create a new feature branch:**
   ```bash
   git checkout -b feature/new-feature
   ```
3. **Commit your changes:**
   ```bash
   git commit -m "Add new feature"
   ```
4. **Push the branch to GitHub:**
   ```bash
   git push origin feature/new-feature
   ```
5. Open a **Pull Request** with a detailed description of your changes.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---