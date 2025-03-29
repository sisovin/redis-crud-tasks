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

Here's the **frontend project structure** for building the **Vue 3 + TypeScript + Vite** setup, aligning with your **backend structure** while following best practices:

---

## **📂 Project Structure (Frontend)**
```
redis_crud_tasks/
│── backend/                          # Django Backend (unchanged)
│── frontend/                         # Frontend (Vue 3 + TypeScript + Vite)
│   │── public/                        # Static assets
│   │   │── favicon.ico
│   │── src/                           # Main frontend source code
│   │   │── api/                       # API requests
│   │   │   │── auth.ts                # Authentication API calls
│   │   │   │── tasks.ts               # Task CRUD API calls
│   │   │── assets/                    # Static assets like images & styles
│   │   │── components/                # Reusable Vue components
│   │   │   │── auth/
│   │   │   │   │── Login.vue
│   │   │   │   │── Register.vue
│   │   │   │── tasks/
│   │   │   │   │── TaskItem.vue        # Single task component
│   │   │   │   │── TaskList.vue        # Task list rendering
│   │   │   │   │── AddTask.vue         # Add new task form
│   │   │   │── ui/
│   │   │   │   │── Button.vue          # Reusable button component
│   │   │   │   │── Modal.vue           # Reusable modal component
│   │   │── composables/                # Vue composables (reusable logic)
│   │   │   │── useAuth.ts              # Handle authentication state
│   │   │   │── useTasks.ts             # Manage task state
│   │   │   │── useFetch.ts             # Fetch wrapper for API calls
│   │   │── layouts/                    # Page layouts
│   │   │   │── DefaultLayout.vue       # Base layout with navbar/sidebar
│   │   │   │── AuthLayout.vue          # Layout for login/register pages
│   │   │── pages/                      # Application pages
│   │   │   │── Home.vue
│   │   │   │── Dashboard.vue
│   │   │   │── Tasks.vue
│   │   │── router/                     # Vue Router setup
│   │   │   │── index.ts                # Routes definition
│   │   │── store/                      # Pinia state management
│   │   │   │── auth.ts                 # Authentication store
│   │   │   │── tasks.ts                # Task store
│   │   │── styles/                     # Global styles
│   │   │   │── main.css
│   │   │   │── variables.css
│   │   │── utils/                      # Utility functions/helpers
│   │   │   │── formatDate.ts           # Date formatting helper
│   │   │   │── validateForm.ts         # Form validation helper
│   │   │── App.vue                     # Main application entry point
│   │   │── main.ts                     # Vue app initialization
│   │── .env                            # Environment variables
│   │── index.html                      # Main HTML file
│   │── package.json                    # Project dependencies
│   │── tsconfig.json                    # TypeScript configuration
│── scripts/
│   │── seed_db.py                      # Backend: Seed database script
│   │── redis_test.py                    # Backend: Redis test script
│── requirements.txt                     # Backend dependencies
│── Dockerfile                           # Dockerfile for frontend & backend
│── docker-compose.yml                   # Docker Compose for full stack
│── manage.py                             # Django management script
│── README.md                             # Project documentation
```

---

## **🔹 Key Adjustments**
✅ **Vite + TypeScript** setup  
✅ **Organized API Calls** in `/src/api/`  
✅ **Reusable Components** under `/src/components/`  
✅ **Vue Composables** for reusable logic (`useAuth.ts`, `useTasks.ts`)  
✅ **Pinia State Management** for authentication & tasks (`store/`)  
✅ **Vue Router Setup** (`router/index.ts`)  
✅ **Global Styles & Utilities** (`styles/`, `utils/`)  
✅ **Layouts for UI Consistency** (`layouts/`)  

---
