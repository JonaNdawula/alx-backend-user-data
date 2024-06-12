#!/usr/bin/env python3
"""
This module contains a flask app
"""
from flask import Flask, jsonify, request, abort, make_response, redirect
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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    Logout function
    """
    session_id = request.cookies.get('session_id')

    user = AUTH.get_user_from_session_id(session_id)

    if user is None or session_id is None:
        abort(403)
    AUTH.destroy_session(user.id)

    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """
    Responds to Get /profile route
    """
    session_id = request.cookies.get('session_id')

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    return jsonify({'email': user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_rest_password_token():
    """
    Responds to POST /reset_password route
    """
    email = request.form.get('email')

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({'email': email, 'reset_token': reset_token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """
    Responds to PUT /reset_password route
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({'email': email, 'message': 'Password updated'}) 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
