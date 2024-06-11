#!/usr/bin/env python3
"""
Module to encrypt  a password
with bcrypt.hashqw
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt


class Auth:
    """Auth class which interacts with database
    for authentication
    """
    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """
        encrypts a password
        """
        salt = bcrypt.gensalt(rounds=12, prefix=b'2b')
        hashed_pass = bcrypt.hashpw(password.encode(), salt)

        return hashed_pass

    def register_user(self, email: str, password: str) -> User:
        """
        Used to register a user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            user = self._db.add_user(email, hashed_password)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates a user login
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False
