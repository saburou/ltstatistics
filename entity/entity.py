# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import sqlite3
import logging


class Entity(metaclass=ABCMeta):

    _DATABASE = 'C:\\Users\\saburou\\Documents\\work\\workspaces\\livetubestatistic\\livetubestatistic.db'

    def __init__(self, database=_DATABASE, tablename=None):
        self.database = database
        self.tablename = tablename

    @staticmethod
    def static_create(row):
        """
        Create Entity by Entity Object.
        :return: 
        """
        NotImplementedError

    def _executequery(self, sql):
        """
        Execute SQL ( Select ).
        :param sql: SQL
        :return: result list.
        """
        result = None
        connection = None

        try:
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            result = cursor.execute(sql).fetchall()
            connection.commit()
        except sqlite3.Error as e:
            logging.error(u"クエリ実行中にエラーが発生しました。sql=" + sql)
            logging.error(str(e))
        finally:
            if connection is not None:
                connection.close()

        return result

    def _executeupdate(self, sql):
        """
        Execute SQL ( Insert / Update ).
        :param sql: SQL
        :return: true: success false: failed
        """
        result = False
        connection = None

        try:
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            result = cursor.execute(sql)
            connection.commit()
        except sqlite3.Error as e:
            logging.error(u"クエリ実行中にエラーが発生しました。sql=" + sql)
            logging.error(str(e))
        finally:
            if connection is not None:
                connection.close()

        return result

    def find(self):
        """
        Select record(s) with self.
        :return: true: record with primarykey false: None
        """
        record = self._executequery(self._getsqlforselect())
        if record is None:
            return []

        result = []
        for row in record:
            result.append(self.static_create(row))
        return result

    def update(self):
        """
        Update table with self.
        :return true: update success. false: update failed.
        """
        return self._executeupdate(self._getsqlforupdate())

    def regist(self):
        """
        Insert into table with self.
        :return true: update success. false: update failed.
        """
        return self._executeupdate(self._getsqlforregist())

    def count(self):
        """
        Count record(s).
        :return: number of record(s).
        """
        result = self._executequery(self._getsqlforcount())
        if result is None:
            return 0

        c = result[0][0]
        return int(c)

    @abstractmethod
    def _getsqlforselect(self):
        """
        Create SQL for select.
        :return: SQL with placeholder for select.
        """
        raise NotImplementedError

    @abstractmethod
    def _getsqlforcount(self):
        """
        Create SQL for count.
        :return: true: exist false: not exist
        """
        raise NotImplementedError

    @abstractmethod
    def _getsqlforregist(self):
        """
        Create SQL for regist.
        :return: SQL with placeholder for regist.
        """
        raise NotImplementedError

    @abstractmethod
    def _getsqlforupdate(self):
        """
        Create SQL fro update.
        :return: SQL with placeholder for update.
        """
        raise NotImplementedError
