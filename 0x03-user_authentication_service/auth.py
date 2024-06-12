#!/usr/bin/env python3
"""
Module to encrypt  a password
with bcrypt.hashqw
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    encrypts a password
    """
    salt = bcrypt.gensalt(rounds=12, prefix=b'2b')
    hashed_pass = bcrypt.hashpw(password.encode(), salt)

    return hashed_pass


def _generate_uuid() -> str:
    """
    Generates a new UUID
    """
    return str(uuid4())


class Auth:
    """Auth class which interacts with database
    for authentication
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Used to register a user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates a user login
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode('utf-8'),
                user.hashed_password
                )
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        creates a new session for a user
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id):
        """
        Gets a user using session id
        """
        if session_id is None:
            return None

        user = self._db.find_by({'session_id': session_id})

        if not user:
            return None

        return user
