# -*- coding: utf-8 -*-
from entity.entity import Entity
import json


class StTotalView(Entity):

    def __init__(self, measuredate=None, amount=None):
        super().__init__(super()._DATABASE, tablename="st_total_view")
        self._measuredate = measuredate
        self._amount = amount

    def get_measuredate(self):
        return self._measuredate

    def get_amount(self):
        return self._amount

    @staticmethod
    def static_create(source):
        if source is None:
            return None
        return StTotalView(source[0], source[1])

    def _getsqlforselect(self):
        sql = 'SELECT measuredate, amount FROM %s WHERE measuredate ="%s"' % (self.tablename, self._measuredate)
        return sql

    def _getsqlforcount(self):
        raise NotImplementedError

    def _getsqlforregist(self):
        sql = 'INSERT INTO %s (measuredate, amount) VALUES("%s","%s")' % (self.tablename, self._measuredate, self._amount)
        return sql

    def _getsqlforupdate(self):
        sql = 'UPDATE %s SET amount="%s" WHERE measuredate="%s"' % (self.tablename, self._amount, self._measuredate)
        return sql

    def findday(self, startdate, enddate):
        sql = 'SELECT strftime("%Y-%m-%d %H:00:00", measuredate), AVG(amount)' + ' FROM %s WHERE measuredate >="%s" AND measuredate < "%s" group by ' % (self.tablename, startdate, enddate) + 'strftime("%Y-%m-%d %H", measuredate) order by measuredate;'
        return self._findintime(sql, startdate, enddate)

    def findmonth(self, startdate, enddate):
        sql = 'SELECT strftime("%Y-%m-%d 00:00:00", measuredate), AVG(amount)' + ' FROM %s WHERE measuredate >="%s" AND measuredate < "%s" group by ' % (self.tablename, startdate, enddate) + 'strftime("%Y-%m-%d", measuredate) order by measuredate;'
        return self._findintime(sql, startdate, enddate)

    def findyear(self, startdate, enddate):
        sql = 'SELECT strftime("%Y-%m-01 00:00:00", measuredate), AVG(amount)' + ' FROM %s WHERE measuredate >="%s" AND measuredate < "%s" group by ' % (self.tablename, startdate, enddate) + 'strftime("%Y-%m", measuredate) order by measuredate;'
        return self._findintime(sql, startdate, enddate)

    def _findintime(self, sql, startdate, enddate):
        record = self._executequery(sql)
        if record is None:
            return []

        result = []
        for row in record:
            result.append(self.static_create(row))
        return result
