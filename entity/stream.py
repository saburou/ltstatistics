# -*- coding: utf-8 -*-
from entity.entity import Entity


class Stream(Entity):

    def __init__(self, id=None, title=None, author=None, startdate=None, viewing=None, view=None, comments=None):
        super().__init__(super()._DATABASE, tablename="stream")
        self._id = id
        self._title = title
        self._author = author
        self._startdate = startdate
        self._viewing = viewing
        self._view = view
        self._comments = comments

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_startdate(self):
        return self._startdate

    def get_viewing(self):
        return self._viewing

    def get_view(self):
        return self._view

    def get_comments(self):
        return self._comments

    @staticmethod
    def static_create(source):
        if source is None:
            return None
        return Stream(source[0], source[1], source[2], source[3])

    def _getsqlforselect(self):
        sql = 'SELECT id, title, author, startdate FROM %s WHERE id ="%s"' % (self.tablename, self._id)
        return sql

    def _getsqlforcount(self):
        sql = 'SELECT count(*) FROM %s WHERE id ="%s"' % (self.tablename, self._id)
        return sql

    def _getsqlforregist(self):
        sql = 'INSERT INTO %s (id, title, author, startdate) VALUES("%s","%s","%s","%s")' % (self.tablename, self._id, self._title, self._author, self._startdate)
        return sql

    def _getsqlforupdate(self):
        sql = 'UPDATE %s SET title ="%s", author="%s", startdate="%s" WHERE id = "%s"' % (self.tablename, self._title, self._author, self._startdate, self._id)
        return sql
