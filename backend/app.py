from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)
CORS(app)

# Database setup
DATABASE_URL = "sqlite:///todo.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Task Model
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    priority = Column(String)

Base.metadata.create_all(bind=engine)

# Get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():

    db = SessionLocal()
    tasks = db.query(Task).all()

    result = []

    for t in tasks:
        result.append({
            "id": t.id,
            "title": t.title,
            "priority": t.priority
        })

    return jsonify(result)


# Add task
@app.route("/tasks", methods=["POST"])
def add_task():

    data = request.json

    db = SessionLocal()

    task = Task(
        title=data["title"],
        priority=data["priority"]
    )

    db.add(task)
    db.commit()

    return jsonify({"message": "Task added"})


# Delete task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    db = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if task:
        db.delete(task)
        db.commit()

    return jsonify({"message": "Task deleted"})


if __name__ == "__main__":
    app.run(debug=True)