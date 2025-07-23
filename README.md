 Django REST API - Employee Management

This is a simple REST API built with Django and Django REST Framework to manage employees with CRUD operations, login, and search functionality.


## Features
- Create, Read, Update, Delete employees
- Search employees by name
- Login with email and password
- Health check endpoint


## API Endpoints
- **GET /** – Health check
- **GET /GET/users** – Get all employees
- **GET /GET/user/<id>** – Get employee by ID
- **POST /POST/users** – Create a new employee
- **PUT /PUT/user/<id>** – Update employee details
- **DELETE /DELETE/user/<id>** – Delete employee
- **GET /GET/search/?name=<name>** – Search employees
- **POST /login** – User login

---

## Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
Create virtual environment and activate:


python -m venv myenv
myenv\Scripts\activate   # Windows
# OR
source myenv/bin/activate  # Linux/Mac

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py makemigrations
python manage.py migrate

Run the server:
python manage.py runserver
