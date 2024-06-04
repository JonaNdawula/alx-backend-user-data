#!/usr/bin/env python3
"""
This module contains functions
for basic authentication
"""
from .auth import Auth
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
        A function thatdecodes a pass
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
