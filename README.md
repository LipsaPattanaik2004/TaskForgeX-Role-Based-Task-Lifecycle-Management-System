# TaskForgeX – Role-Based Task Lifecycle Management System

## __Overview__
TaskForgeX is a backend-driven task lifecycle management system designed to simulate a simplified enterprise project tracking platform.  
The system allows users to create, assign, update, and track tasks through a structured workflow using role-based access and database integration.
This project demonstrates practical backend engineering concepts such as REST APIs, CRUD operations, authentication mechanisms, and structured database management.

---
__Key Features__

- Role-based user authentication (Admin / User)
- Task creation, assignment, and lifecycle tracking
- Full CRUD operations for task management
- RESTful API architecture
- SQL database integration
- Modular and maintainable backend structure
- Error handling and debugging support
- Scalable system design for task workflow automation

---

__Technology Stack__

- Programming Language: Python
- Framework: Flask
- Database: SQLite / SQL
- ORM: Flask-SQLAlchemy
- API Style: REST APIs

---

__System Architecture__

The project follows a modular backend architecture:

- __Authentication Module__
  - Handles user registration and login
  - Implements role-based access control

- __Task Management Module__
  - Task creation
  - Task update and status modification
  - Task deletion
  - Task viewing and tracking

- __Database Layer__
  - Stores user and task data
  - SQL-based data management using ORM

---

__Database Structure__

Two primary entities are used:

__User Table__

- User ID
- Username
- Password
- Role

__Task Table__

- Task ID
- Title
- Description
- Assigned User
- Status
- Creation Timestamp

---

__Project Structure__

```
TaskForgeX
│
├── app.py
├── models.py
├── database.py
├── auth.py
├── task_routes.py
├── config.py
├── requirements.txt
└── README.md
```

---

__Installation & Setup__

1. Clone the repository

```
git clone https://github.com/yourusername/TaskForgeX.git
cd TaskForgeX
```

2. Install required dependencies

```
pip install -r requirements.txt
```

3. Run the application

```
python app.py
```

4. Access the API locally

```
http://127.0.0.1:5000/
```

---

__API Functionalities__

The system supports the following operations:

__User APIs__

- Register new user
- Login user
- Role-based authentication

__Task APIs__

- Create a new task
- View all tasks
- Update task details
- Delete task
- Assign task to a user
- Track task status

---

__Skills Demonstrated__

This project highlights key software engineering competencies:

- Programming logic implementation
- Object-Oriented Programming concepts
- REST API development
- Database design and integration
- CRUD operations
- Modular application architecture
- Debugging and error handling

---

__Use Case__

TaskForgeX simulates a lightweight project management system similar to tools like Jira or Trello, allowing teams to manage tasks and track project progress efficiently.

---

__Future Enhancements__

Potential improvements for the system:

- JWT-based authentication
- Frontend dashboard using React
- Task priority and deadline tracking
- Notification system for task updates
- Deployment using Docker and cloud services

---

__Author__

Lipsa Pattanaik  
Aspiring Software Engineer  

LinkedIn:  
http://www.linkedin.com/in/lipsa-pattanaik-196b2a285

---

__License__

This project is created for educational and demonstration purposes.
