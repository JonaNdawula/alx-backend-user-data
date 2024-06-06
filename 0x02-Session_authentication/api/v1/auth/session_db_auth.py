#!/usr/bin/env python3
"""Module contianing Methods and a Class  for DB authentication
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(sessionExpAuth):
    """class containsing methods for DB session Authentication
    """
    def create_session(self, user_id=None):
        """Method to create a session
        """
        session_id = super().create_session(user_id)
        if session_id:
            user_session = UserSession(user_id=user_id, session_id=session_id)
            user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Method to search for session_id
        """
        user_session = UserSession.search({'session_id': session_id})
        if user_session:
            return user_session[0].user_id
        return None

    def destroy_session(self, request=None):
        """Method to destroy session
        """
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                user_seeion = UserSession.search({'session_id': session_id})
                for user_session in user_sessions:
                    user_session.remove()
                return True
        return False
