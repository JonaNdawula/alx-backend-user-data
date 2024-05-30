#!/usr/bin/env python3
"""
This module contains password encrypting
functions
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    This function enrypts a password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    This function is used to validate
    a password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
