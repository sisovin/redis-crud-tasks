# Redis CRUD Tasks

This project is a task management system with a backend built using Django and Django Rest Framework (DRF). It includes features such as user authentication with JWT and MFA, role-based access control, task CRUD operations with Redis caching, and more.

## Project Structure

```
redis_crud_tasks/
│── backend/                          # Backend project (Django + DRF)
│   │── api/
│   │   │── __init__.py
│   │   │── urls.py                    # API Endpoints
│   │   │── views.py                   # API Views
│   │   │── serializers.py             # API Serializers
│   │   │── permissions.py             # Role-based access control (RBAC)
│   │── authentication/
│   │   │── __init__.py
│   │   │── models.py                  # User model with Argon2 password hashing
│   │   │── views.py                   # Authentication logic (JWT + MFA)
│   │   │── serializers.py             # Auth serializers
│   │   │── otp.py                     # OTP (One-Time Password) generator
│   │   │── tokens.py                  # JWT and Refresh Token handling
│   │── tasks/
│   │   │── __init__.py
│   │   │── models.py                  # Task model with soft delete
│   │   │── views.py                   # Task CRUD views with Redis caching
│   │   │── serializers.py             # Task serializers
│   │── config/
│   │   │── __init__.py
│   │   │── settings.py                # Django settings (Redis, ChromaDB, Argon2, JWT)
│   │   │── urls.py                     # Main URL routing
│   │   │── wsgi.py                     # WSGI application
│   │── middleware/
│   │   │── __init__.py
│   │   │── caching.py                 # Custom Redis caching middleware
│   │   │── ratelimit.py               # Rate limiting middleware using Redis
│   │── utils/
│   │   │── __init__.py
│   │   │── redis_utils.py             # Redis utility functions
│   │   │── chromadb_utils.py          # ChromaDB functions
│   │   │── argon2_utils.py            # Password hashing utilities
│   │── App.js
│   │── index.js
│   │── package.json
│── scripts/
│   │── seed_db.py                     # Script to seed database with dummy tasks
│   │── redis_test.py                   # Script to test Redis caching
│── requirements.txt                     # Python dependencies
│── Dockerfile                           # Dockerfile for deployment
│── docker-compose.yml                   # Compose file for Redis, PostgreSQL, Django
│── manage.py                             # Django management script
│── README.md                             # Project documentation
```

## Setup and Running the Project

### Prerequisites

- Docker
- Docker Compose
- Python 3.8+
- Redis
- PostgreSQL

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/githubnext/workspace-blank.git
   cd redis_crud_tasks
   ```

2. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the Docker containers:
   ```sh
   docker-compose up --build
   ```

5. Apply the migrations:
   ```sh
   docker-compose exec web python manage.py migrate
   ```

6. Seed the database with dummy tasks:
   ```sh
   docker-compose exec web python scripts/seed_db.py
   ```

### Running the Project

1. Start the development server:
   ```sh
   docker-compose up
   ```

2. The project will be available at `http://localhost:8000`.

## Using the API Endpoints

### Authentication

- **Login**: `POST /api/auth/login/`
- **Register**: `POST /api/auth/register/`
- **Refresh Token**: `POST /api/auth/refresh/`
- **Verify OTP**: `POST /api/auth/verify-otp/`

### Tasks

- **List Tasks**: `GET /api/tasks/`
- **Create Task**: `POST /api/tasks/`
- **Retrieve Task**: `GET /api/tasks/{id}/`
- **Update Task**: `PUT /api/tasks/{id}/`
- **Delete Task**: `DELETE /api/tasks/{id}/`
