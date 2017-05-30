# -*- coding: utf-8 -*-
from entity.entity import Entity


class StComment(Entity):

    def __init__(self, id=None, measuredate=None, amount=None):
        super().__init__(super()._DATABASE, tablename="st_comment")
        self._id = id
        self._measuredate = measuredate
        self._amount = amount

    @staticmethod
    def static_create(source):
        if source is None:
            return None
        return StComment(source[0], source[1], source[2])

    def _getsqlforselect(self):
        sql = 'SELECT id, measuredate, amount FROM %s WHERE id ="%s"' % (self.tablename, self._id)
        return sql

    def _getsqlforcount(self):
        sql = 'SELECT count(*) FROM %s WHERE id ="%s" and measuredate = "%s"' % (self.tablename, self._id, self._measuredate)
        return sql

    def _getsqlforregist(self):
        sql = 'INSERT INTO %s (id, measuredate, amount) VALUES("%s","%s","%s")' % (self.tablename, self._id, self._measuredate, self._amount)
        return sql

    def _getsqlforupdate(self):
        sql = 'UPDATE %s SET measuredate ="%s", amount="%s" WHERE id="%s"' % (self.tablename, self._measuredate, self._amount, self._id)
        return sql

