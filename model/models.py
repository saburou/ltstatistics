# -*- coding: utf-8 -*-
import sqlalchemy.ext.declarative
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DATETIME

Base = sqlalchemy.ext.declarative.declarative_base()


class StComment(Base):
    __tablename__ = 'st_comment'
    id = Column(String, primary_key=True)
    date = Column(DATETIME, primary_key=True)
    amount = Column(Integer)

    def __repr__(self):
        return "<StComment('%s', '%s', '%s')>" % (self.id, self.date, self.amount)

    @staticmethod
    def select(cls, target_id, session):
        return session.query(StComment).filter(StComment.id == target_id).all()

    @staticmethod
    def count(cls, target_id, target_date, session):
        return session.query(StComment).filter(StComment.id == target_id, StComment.date == target_date).count()

    @staticmethod
    def regist(cls, target_id, target_date, target_amount, session):
        session.add(StComment(id=target_id, date=target_date, amount=target_amount))

    @staticmethod
    def update(cls, target_id, target_date, target_amount, session):
        session.add(StComment(id=target_id, date=target_date, amount=target_amount))


class StTotalView(Base):

    __tablename__ = 'st_total_view'
    date = Column(DATETIME, primary_key=True)
    amount = Column(Integer)

    def __repr__(self):
        return "<StTotalView('%s','%s')>" % (self.date, self.amount)

    @staticmethod
    def select(cls, target_date, session):
        return session.query(StTotalView).filter(StTotalView.date == target_date).all()

    @staticmethod
    def count(cls, target_date, session):
        return session.query(StTotalView).filter(StTotalView.date == target_date).count()

    @staticmethod
    def regist(cls, target_date, target_amount, session):
        session.add(StTotalView(date=target_date, amount=target_amount))

    @staticmethod
    def update(cls, target_date, target_amount, session):
        session.add(StTotalView(date=target_date, amount=target_amount))


class StView(Base):

    __tablename__ = 'st_view'
    id = Column(String, primary_key=True)
    date = Column(DATETIME, primary_key=True)
    amount = Column(Integer)

    def __repr__(self):
        return "<StView('%s', '%s', '%s')>" % (self.id, self.measuredate, self.amount)

    @staticmethod
    def count(cls, target_id, target_date, session):
        return session.query(StView).filter(StView.id == target_id, StView.date == target_date).count()

    @staticmethod
    def select(cls, target_id, session):
        return session.query(StView).filter(StView.id == target_id).all()

    @staticmethod
    def regist(cls, target_id, target_date, target_amount, session):
        session.add(StView(id=target_id, date=target_date, amount=target_amount))

    @staticmethod
    def update(cls, target_id, target_date, target_amount, session):
        session.add(StView(id=target_id, date=target_date, amount=target_amount))


class Stream(Base):

    __tablename__ = 'stream'
    id = Column(String, primary_key=True)
    title = Column(String)
    author = Column(String)
    startdate = Column(DATETIME)
    viewing = Column(Integer)
    comments = Column(Integer)

    def __repr__(self):
        return "<Stream('%s', '%s', '%s', '%s')>" % (self.id, self.title, self.author, self.startdate)

    @staticmethod
    def select(cls, target_id, session):
        return session.query(Stream).filter(Stream.id == target_id).all()

    @staticmethod
    def count(cls, target_id, session):
        return session.query(Stream).filter(Stream.id == target_id).count()

    @staticmethod
    def regist(cls, target_id, target_title, target_author, target_startdate, session):
        session.add(Stream(id=target_id, title=target_title, author=target_author, startdate=target_startdate))

    @staticmethod
    def update(cls, target_id, target_title, target_author, target_startdate, session):
        # session.add(Stream(id=target_id, title=target_title, author=target_author, startdate=target_startdate))
        raise NotImplementedError

if __name__ == "__main__":
    schema = 'sqlite:///../core/database.sqlite3'
    engine = create_engine(schema, echo=True)
    Base.metadata.create_all(engine)
