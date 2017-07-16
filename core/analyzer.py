# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from datetime import datetime
from model.models import Stream, StTotalView, StView, StComment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Analyzer(metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def analyze(self, data):
        """
        Analyze data.
        :param data: target data. 
        :return: data analyzed.
        """
        raise NotImplementedError

Engine = create_engine('sqlite:///database.sqlite3', echo=True)


class ViewAnalyzer(Analyzer):
    """
    Analysis stream viewing information.
    """
    def analyze(self, data):

        _SESSION = sessionmaker(bind=Engine)
        session = _SESSION()

        currentdate = datetime.now()
        # Regist individual stream view.
        total = 0
        for d in data:
            if not isinstance(d, Stream):
                continue
            # Regist viewing.
            view = StView(id=d.id, date=currentdate, amount=d.viewing)
            if view.count(StView, d.id, currentdate, session) > 0:
                view.update(StView, d.id, currentdate, d.viewing, session)
            else:
                view.regist(StView, d.id, currentdate, d.viewing, session)
            total += int(d.viewing)
            # Regist comments.
            comment = StComment(id=d.id, date=currentdate, amount=d.comments)
            if comment.count(StComment, d.id, currentdate, session) > 0:
                comment.update(StComment, d.id, currentdate, d.comments, session)
            else:
                comment.regist(StComment, d.id, currentdate, d.comments, session)
        # Regist total stream view.
        totalview = StTotalView(date=currentdate, amount=total)
        totalview.regist(StTotalView, currentdate, total, session)

        session.commit()
        session.close()
