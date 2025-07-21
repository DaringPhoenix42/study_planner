# 📖 Study Planner

Study Planner is a **modular Django web application** for students and lifelong learners to organize notes, homework, to-dos, and educational resources in one place. The platform features a clean, responsive interface and robust user management.

---

## Table of Contents
- [Features](#features)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Use Cases](#use-cases)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- **User Authentication:** Registration, login, logout, and profile management with avatar upload (Django-allauth).
- **Notes:** Create, edit, categorize, and tag personal study notes.
- **Homework:** Track assignments with due dates and completion status.
- **To-Do List:** Manage daily tasks with priorities and completion tracking.
- **Resources:** Organize books, YouTube videos (with thumbnail extraction), and Wikipedia articles (with title parsing).
- **Dashboard:** Unified overview of all your academic data.
- **Search & Pagination:** Find and filter notes, homework, to-dos, and resources efficiently.
- **Responsive UI:** Mobile-first design using Bootstrap4 and FontAwesome icons.

---

## Screenshots
<!-- Add screenshots/gifs here to showcase the UI -->

---

## Tech Stack
- **Backend:** [Django](https://www.djangoproject.com/) (Python)
- **Frontend:** HTML, CSS, JavaScript, [Bootstrap4](https://getbootstrap.com/)
- **Database:** SQLite (default; easily swappable for PostgreSQL/MySQL)
- **Icons:** [FontAwesome](https://fontawesome.com/)

---

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YourUsername/study_planner.git
   cd study_planner
   ```
2. **Create & Activate a Virtual Environment:**
   - Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   ```dotenv
   DEBUG=True
   SECRET_KEY=your-secret-key
   DATABASE_URL=sqlite:///db.sqlite3
   STUDY_PLANNER_ENV=development
   ```
5. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. **Create a Superuser:**
   ```bash
   python manage.py createsuperuser
   ```
7. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```
   Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Project Structure
```
study_planner/
├── study_planner/      # Project settings, URLs, WSGI
├── users/              # User authentication & profile
├── notes/              # Notes management
├── homework/           # Homework tracking
├── todo/               # To-do list
├── resources/          # Educational resources (books, YouTube, Wikipedia)
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

---

## Configuration
- **DEBUG:** Set to `True` for development.
- **SECRET_KEY:** Django secret key.
- **DATABASE_URL:** Database connection string.
- **STUDY_PLANNER_ENV:** Custom environment variable.

---

## Use Cases
- **Students:** Centralize notes, assignments, and resources.
- **Educators:** Base for a school/university portal.
- **Productivity:** Adaptable for general task/resource management.

---

## Contributing
1. **Fork** the repository.
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature
   ```
3. **Commit your changes:**
   ```bash
   git commit -m "Describe your feature"
   ```
4. **Push and open a Pull Request.**

---

## License
MIT License. See [LICENSE](LICENSE) for details.

---

## Acknowledgements
- Django community for documentation and support.
- [Bootstrap](https://getbootstrap.com/) for UI components.
- [FontAwesome](https://fontawesome.com/) for icons.

---

**Happy Learning! 🚀**