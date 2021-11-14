# Insecure Books App

A simple insecure books app to demonstrate SQL Injection and Buffer Overflow attacks with Python/Django

## Getting Started

- Create a virtual environment `python3 -m venv venv` OR `python -m venv venv`

- Activate the virtual environment `source venv/bin/activate`

- Install dependencies `pip install -r requirements.txt`

- To start the server locally `python manage.py runserver`

### Admin Dashboard

- Go to `http://localhost:8000/admin/`

- Enter user credentials - Username: `admin`, Password: `complex_password`

### SQL Injection Attack

- In the search field enter the search term `new` and no results show

- When you enter this `new%' --` you get no results as th bug has been fixed

### Buffer Overflow Attack

- Start the server and click the titles link. The server no longer stops because enough space has been allocated.
