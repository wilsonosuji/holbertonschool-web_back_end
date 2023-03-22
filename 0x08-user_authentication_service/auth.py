#!/usr/bin/env python3
""" User authentication service """
import bcrypt
from db import DB
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


def _hash_password(password: str) -> str:
    """ Hash password method """
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Constructor method """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register_user method """
        try:
            register = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_p = _hash_password(password)
            register_user = self._db.add_user(email, hashed_p)
            return register_user
        raise ValueError("User {} already exists.".format(register.email))


def _generate_uuid() -> str:
    """ Generarrte UUIDs """
    return str(uuid.uuid4())
