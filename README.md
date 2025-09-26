Event Booking System

Overview

A Django-based Event Booking System that allows users to register, login, browse events, and book tickets. Admins can manage events and view all bookings.

Features

User registration and login with custom user model
View all available events
Book tickets for an event
Admin dashboard to manage events and bookings
Track booking status (Pending, Confirmed, Cancelled)
Technology Stack

Backend: Python, Django 4.2
Database: SQLite (or PostgreSQL/MySQL)
Frontend: HTML, CSS, Bootstrap
Authentication: Django built-in + custom user model
Project Structure

Setup Instructions

Clone the repository
git clone https://github.com/yourusername/event_booking_system.git
cd event_booking_system
2.Create and activate virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate


3.Install dependencies

pip install -r requirements.txt


4.Apply migrations

python manage.py makemigrations
python manage.py migrate


5.Create superuser (admin)

python manage.py createsuperuser


Run the server

python manage.py runserver


6.Open in browser

http://127.0.0.1:8000/
for admin:http://127.0.0.1:8000/admin/
