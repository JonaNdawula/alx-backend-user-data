#!/usr/bin/env python3
"""
This module has classes and methods used
for session authenntication
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    This class inherits from Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Method that creates a session
        """
        if user_id is None or type(user_id) != str:
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
