# Smart Todo App

A simple full-stack Todo application built using **React**, **Flask**, and **SQLite**.  
This project allows users to manage daily tasks by adding, viewing, and deleting tasks with priority levels.

---

## Features

- Add new tasks
- Set task priority (High, Medium, Low)
- View all tasks
- Delete completed tasks
- REST API communication between frontend and backend

---

## Tech Stack

Frontend: React  
Backend: Python Flask  
Database: SQLite  
API Communication: REST API (JSON)

---

## Project Structure

smart-todo-app  
│  
├── backend  
│   └── app.py  
│  
├── frontend  
│   └── src  
│  
└── README.md  

---

## Key Technical Decisions

### 1. Flask for Backend
Flask was chosen because it is lightweight and suitable for building simple REST APIs quickly. It allows easy integration with databases and works well for small projects.

### 2. React for Frontend
React was used to create a dynamic and interactive user interface. It allows efficient state management and updates the UI without reloading the page.

### 3. SQLite as Database
SQLite was selected as the database because it is lightweight, serverless, and easy to set up for small applications.

### 4. REST API Communication
The frontend communicates with the backend using REST APIs. React sends HTTP requests (GET, POST, DELETE) to the Flask server, which processes the request and returns JSON responses.

### 5. Component-based UI
React components were used to keep the frontend code modular and maintainable.

---

## How to Run the Project

### Backend

cd backend  
python app.py  

The backend server will run on:  
http://127.0.0.1:5000

### Frontend

cd frontend  
npm start  

The frontend application will run on:  
http://localhost:3000

---

## Example API Endpoints

GET /tasks → Get all tasks  
POST /tasks → Add a new task  
DELETE /tasks/{id} → Delete a task  

---

## Author

Abhishek Prasad