#!/usr/bin/env python3
"""
This module contains a flask app
"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """
    returns the / page
    """
    return jsonify({'message': 'Bienvenue'})


if __name__ == "__main__main":
    app.run(host="0.0.0.0", port=5000)
