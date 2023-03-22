#!/usr/bin/env python3
""" User authentication service """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import User


from user import Base


class DB:
    """ DB Class: database """
    def __init__(self):
        """ Constructor method """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ create session """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ add_user method """
        add_u = User(email=email, hashed_password=hashed_password)
        self._session.add(add_u)
        self._session.commit()
        return add_u

    def find_user_by(self, **kwargs) -> User:
        """ findy_user_by method """
        find = self._session.query(User).filter_by(**kwargs).first()
        if find is None:
            raise NoResultFound
        return find

    def update_user(self, user_id: int, **kwargs) -> None:
        """ update_user method """
        update = self.find_user_by(id=user_id)
        columns = User.__table__.columns._data.keys()
        for key, value in kwargs.items():
            if key in columns:
                setattr(update, key, value)
            else:
                raise ValueError
        self._session.commit()
