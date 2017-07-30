# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBSessionFactory:
    SCHEMA = 'sqlite:///database.sqlite3'
    ENGINE = create_engine(SCHEMA, echo=True)

    @staticmethod
    def create():
        """
        Create database session.
        :return: database session
        """
        _SESSION = sessionmaker(bind=DBSessionFactory.ENGINE)
        return _SESSION()
