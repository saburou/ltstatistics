# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from datetime import datetime
from model.models import Stream, StTotalView, StView, StComment
from core.session import DBSessionFactory


class Register(metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def regist(self, data):
        """
        Analyze data.
        :param data: target data. 
        :return: data analyzed.
        """
        raise NotImplementedError


class ViewRegister(Register):
    """
    Regist stream viewing information into database.
    """
    def regist(self, data):
        session = DBSessionFactory.create()

        currentdate = datetime.now()
        total = 0
        for d in data:
            if not isinstance(d, Stream):
                continue
            # Regist viewing.
            view = StView(id=d.id, date=currentdate, amount=d.viewing)
            if view.count(d.id, currentdate, session) > 0:
                view.update(d.id, currentdate, d.viewing, session)
            else:
                view.regist(d.id, currentdate, d.viewing, session)
            total += int(d.viewing)
            # Regist comments.
            comment = StComment(id=d.id, date=currentdate, amount=d.comments)
            if comment.count(d.id, currentdate, session) > 0:
                comment.update(d.id, currentdate, d.comments, session)
            else:
                comment.regist(d.id, currentdate, d.comments, session)
        # Regist total stream view.
        totalview = StTotalView(date=currentdate, amount=total)
        totalview.regist(currentdate, total, session)

        session.commit()
        session.close()


class StreamRegister(Register):
    """
    Regist stream information.
    """
    def regist(self, data):
        session = DBSessionFactory.create()
        for s in data:
            if s is None:
                continue
            if Stream.count(target_id=s.id, session=session) == 0:
                Stream.regist(target_id=s.id, target_title=s.title, target_author=s.author,
                              target_startdate=s.startdate, session=session)

        session.commit()
        session.close()
