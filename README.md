# Django Discussion Board - Final Project

The goal of this project was to go from the basic intro applications to gaining hands-on experience developing a real-world application. This project helped me practice writing clean and maintainable code using Django. This app allows users to browse discussion categories, create discussion threads and participate in conversations by posting replies.

---

## Key Features

**Board & Topic Management:**
- Display A List Of Discussion Boards On The Homepage
- Dynamic URLs For Viewing Topics Within Specific Boards
- Ability To Create New Topics With A Subject & Initial Message

**User Authentication System:**
- User Sign-Up, Log-In & Log-Out Functionality
- Password Reset Through Email Simulation
- User Profile Management & Account Updates

**Interaction & Posting:**
- Reply System For Users To Comment On Exisiting Topics
- Post Editing Functionality For Author (Original)

**Advanced Functionality:**
- Pagination For Managing Large Lists Of Topics & Posts
- Search & Filtering Using Django ORM Queries
- Unit Testing To Verify Application Functionality

**Tech Stack:**
- HTML5, CSS3, Bootstrap 4, Python 3, Django, SQLite (Development), PostgreSQL, Virtualenv & Pip.

---

## Installation & Setup

1. Clone The Repository
```text
git clone https://github.com/your-username/django-discussion-board.git cd django-discussion-board
```text

2. Create & Activate A Virtual Environment
```text
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```texct

3. Install Project Dependencies
```text
pip install -r requirements.txt
```text

4. Apply Database Migrations
```text
python manage.py migrate
```text

5. Run The Development Server
```text
python manage.py runserver
```text

6. Open The Application In Your Browser
```text
http://127.0.0.1:8000/
```text

---

## Installation & Setup

```text
django-discussion-board/
│
├── boards/      # App Handling Boards, Topics & Posts
├── accounts/    # App Handling User Authentication & Profiles
├── templates/   # HTML Templates
├── static/      # CSS, JavaScript & Images
├── manage.py    # Django Management Script
└── db.sqlite3   # Development Database
```text

---

## Learning Outcomes

Through this project I gained experience with:

(1). Building A Complete Web Application Using Django
(2). Designing Database Models & Implementing Authentication Systems
(3). Managing Dynamic Content w/ Django Views & Templates
(4). Following Clean Code & Maintainable Project Structure Practices

---

*Ruaa Abdelrahman*
