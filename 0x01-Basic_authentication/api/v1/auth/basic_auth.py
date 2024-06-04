#!/usr/bin/env python3
"""
This module contains functions
for basic authentication
"""
from .auth import Auth


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
