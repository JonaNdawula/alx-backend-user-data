#!/usr/bin/env python3
"""
This module contains functions
for basic authentication
"""
from .auth import Auth
from models.user import User
from typing import TypeVar
import base64


class BasicAuth(Auth):
    """
    Class doing basic authentication
    """
    def extract_base64_authorization_header(
                                            self, authorization_header: str
                                           ) -> str:
        """
        A function doing basic authentication
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
                                           self,
                                           base64_authorization_header: str
                                          ) -> str:
        """
        A function that decodes
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
                                 self,
                                 decoded_base64_authorization_header: str
                                ) -> (str, str):
        """
        A function that returns
        the user email and password
        from Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_email, user_password = decoded_base64_authorization_header.split(
                                    ':', 1
                                    )
        return user_email, user_password

    def user_object_from_credentials(
                                     self, user_email: str, user_pwd: str
                                   ) -> str:
        """
        A function that returns the User
        instance based on his email and password
        """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        users = User.search({'email': user_email})
        if not users:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
