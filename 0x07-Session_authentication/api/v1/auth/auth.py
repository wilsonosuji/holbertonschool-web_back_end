#!/usr/bin/env python3
""" Manage the API authentication """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class Auth for API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require authentication """
        if excluded_paths in [None, []]:
            return True
        if path == "/api/v1/status/" or path == "/api/v1/status":
            return False
        if path is None or path not in excluded_paths:
            return True
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """ Authorization header """
        if request is None:
            return None

        req_header = request.headers.get("Authorization")
        return req_header

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User """
        return None
