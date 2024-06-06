#!/usr/bin/env python3
"""
This module authenticates sessions
"""
from flask import Blueprint, request, jsonify, make_response
from models.user import User
from api.v1.app import auth
from os import getenv
from api.v1.app import app


SESSION_NAME = getenv("SESSION_NAME")

session_auth = Blueprint(
    'session_auth', __name__,
    url_prefix='/api/v1/auth_session'
)


@session_auth.route('/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    Method to log in
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error", "no user found for this email"})

    for user in users:
        if user.is_valid_password(password):
            session_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            response.set_cookie(getenv("SESSION_NAME"), session_id)
            return response

@session_auth.route('/logut', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    Method to delete
    """
    if not auth.detroy_session(request):
        abort(404)
    return jsonify({}), 200
