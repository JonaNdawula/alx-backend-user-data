#!/usr/bin/env/ python3
"""
module constains password encrypting
functions
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    This function enrypts a password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
