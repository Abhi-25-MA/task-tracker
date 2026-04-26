# Django Task Tracker

A full-stack Task Management application that allows users to organize their daily activities, set deadlines, and track completion status.

## 🚀 Features
- **User Authentication:** Secure Signup, Login, and Logout functionality.
- **Task Management:** Create, Edit, Update, and Delete (CRUD) tasks.
- **Deadline Tracking:** Set due dates for tasks to stay organized.
- **Responsive UI:** Built with **Bootstrap 5** for a modern look on mobile and desktop.
- **Deployment Ready:** Configured for seamless hosting on **Render**.

## 🛠️ Tech Stack
- **Backend:** Django 5.2 (Python)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (Development)
- **Deployment:** Render + Gunicorn + WhiteNoise

## 📦 Installation & Setup

1. Clone the repository:
   git clone [https://github.com/Abhi-25-MA/task-tracker.git](https://github.com/Abhi-25-MA/task-tracker.git)
   cd task-tracker
   
2.Install dependencies:
pip install -r requirements.txt

3.Apply migrations:
python manage.py migrate

4.Run the server:
python manage.py runserver
