# Django Discussion Board (Beginner Project)

This is a simple Django forum built step‑by‑step for learning.

## Features
- Boards list (homepage)
- Topics inside a board
- Create new topic + first post
- View topic posts + reply
- Post editing (author only)
- Authentication: sign‑up, log‑in, log‑out
- Password reset (console email)
- Profile update
- Pagination + search
- Basic unit tests

## Setup (Windows PowerShell)
```text
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install django
py manage.py migrate
py manage.py runserver
```

## Create Admin User
```text
py manage.py createsuperuser
```
Then visit: http://127.0.0.1:8000/admin/

## Demo Checklist
1. Home page shows boards
2. Board page shows topics + search + pagination
3. Create new topic (logged in)
4. View topic posts + reply
5. Edit your own post
6. Sign up / log in / log out
7. Password reset (check terminal output)
8. Update profile info

## Run Tests
```text
py manage.py test
```
