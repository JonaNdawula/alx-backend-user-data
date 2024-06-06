#!/usr/bin/env python3
"""
This module authenticates sessions
"""
from flask import Blueprint, request, jsonify, make_response
from models.user import User
from api.v1.app import auth
from os import getenv


SESSION_NAME = getenv("SESSION_NAME")

session_auth = Blueprint(
    'session_auth', __name__,
    url_prefix='/api/v1/auth_session'
)


@session_auth.route('/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    email = request.form.get('email')
    password = request.form.get('password')
    users = User.search({"email": email})

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = make_response(user.to_json())
    response.set_cookie(SESSION_NAME, session_id)
    return response
