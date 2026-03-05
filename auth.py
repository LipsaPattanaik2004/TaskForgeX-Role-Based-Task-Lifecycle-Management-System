from flask import request, jsonify
from models import db, User

def register():
    data = request.json

    user = User(
        username=data["username"],
        password=data["password"],
        role="user"
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered"})
