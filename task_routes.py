from flask import request, jsonify
from models import db, Task

def create_task():
    data = request.json

    task = Task(
        title=data["title"],
        description=data["description"],
        assigned_to=data["assigned_to"],
        status="OPEN"
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task created"})
