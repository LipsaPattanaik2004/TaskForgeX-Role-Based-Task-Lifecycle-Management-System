from flask import Blueprint, request, jsonify
from models import User
from database import db
from response_formatter import success_response, error_response

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.json

    if "username" not in data or "password" not in data:
        return jsonify(error_response("Missing credentials")), 400

    user = User(
        username=data["username"],
        password=data["password"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify(success_response("User registered successfully"))
