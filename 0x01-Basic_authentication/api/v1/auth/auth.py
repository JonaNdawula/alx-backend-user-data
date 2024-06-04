#!/usr/bin/env python3
"""Auth module
"""
from flask import request
from typing import List, TypeVar


User = TypeVar('user')


class Auth:
    """
    A class for API  Authenticattion
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        function for authentication
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        if path[-1] != '/':
            path += '/'
        for exc_path in excluded_paths:
            if exc_path[-1] == '*':
                if path.startswith(exc_path[:-1]):
                    return False
                elif path == exc_path:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        function returning value
        of header request
        """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> User:
        """
        function returning None
        """
        return None
