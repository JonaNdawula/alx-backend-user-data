#!/usr/bin/env python3
"""
MOdule contains functions that
add an expiration date to a Session ID.
"""
from api.v1.auth.session_suth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """
    Class with functions that
    add an expiration date to a Session ID.
    """
    def __init__(self):
        super().__init__()
        try:
            self.session_duration = int(getenv("SESSION_DURATION"))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Method creates a session
        """
        session_id = super().create_session(user_id)
        if session_id:
            self.user_id_by_session_id[session_id] = {
                'user_id': user_id,
                'created_at': datetime.now()
            }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Method to show session Id
        """
        if session_id and session_id in self.user_id_by_session_id:
            session_dict = self.user_id_by_session_id[session_id]
            if self.session_duration <= 0:
                return session_dict['user_id']
            if 'created_at' in session_dict:
                if datetime.now() < session_dict['creared_at']
                + timedelta(seconds=self.session_duration):
                    return session_dict['user_id']
                None
