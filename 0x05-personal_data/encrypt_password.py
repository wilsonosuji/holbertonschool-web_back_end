#!/usr/bin/env python3
""" Encript password """
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash password: returns a salted, hashed password, which is a byte string
    """
    pswd = password.encode()
    hashed = bcrypt.hashpw(pswd, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Is Valid """
    validate = password.encode()
    if bcrypt.checkpw(validate, hashed_password):
        return True
    else:
        return False
