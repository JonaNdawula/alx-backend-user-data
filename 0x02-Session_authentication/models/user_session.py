#!/usr/bin/env python3
"""Module for users
"""
from models.base import Base


class UserSession(Base):
    """Class for user session
    """
    def __init__(self, *args: list, **kwargs: dict):
        """Method for user session
        """
        super().__init__(*args, kwargs)
        self.user_id = kwargs.get('user_id')
        self.session('session_id')
