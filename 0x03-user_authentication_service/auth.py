#!/usr/bin/env python3
"""
Module to encrypt  a password
with bcrypt.hashqw
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    encrypts a password
    """
    hashed_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    return hashed_pass
