from flask import Blueprint, request, jsonify
from models import Task
from database import db
from task_validator import validate_task_data
from response_formatter import success_response, error_response

task_bp = Blueprint("tasks", __name__)


@task_bp.route("/tasks", methods=["POST"])
def create_task():

    data = request.json

    valid, message = validate_task_data(data)

    if not valid:
        return jsonify(error_response(message)), 400

    task = Task(
        title=data["title"],
        description=data["description"],
        assigned_to=data["assigned_to"],
        status="OPEN"
    )

    db.session.add(task)
    db.session.commit()

    return jsonify(success_response("Task created successfully"))


@task_bp.route("/tasks", methods=["GET"])
def get_tasks():

    tasks = Task.query.all()

    task_list = []

    for task in tasks:

        task_list.append({
            "id": task.id,
            "title": task.title,
            "status": task.status
        })

    return jsonify(success_response("Tasks fetched", task_list))
