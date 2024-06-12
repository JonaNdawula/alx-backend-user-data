#!/usr/bin/env python3
"""
This module contains a flask app
"""
from flask import Flask, jsonify, request, abort, make_response
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """
    returns the / page
    """
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
    returns users route
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({'email': email, 'message': 'user created'})
    except ValueError:
        return jsonify({'message': 'email already resgistered'}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    Login function
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)

    response = make_response(
               jsonify({'email': email, 'message': 'logged in'}), 200)
    response.set_cookie('session_id', session_id)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
