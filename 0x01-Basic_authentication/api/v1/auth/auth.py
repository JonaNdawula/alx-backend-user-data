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

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """
        function retutning None
        """
        return None

    def current_user(self, request=None) -> User:
        """
        function returning None
        """
        return None
