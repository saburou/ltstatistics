# -*- coding: utf-8 -*-
from datetime import datetime, timedelta


class DateUtils:

    @staticmethod
    def parse(date):
        dateparams = date.split("-")
        year = dateparams[0]
        month = dateparams[1]
        day = dateparams[2]
        return datetime(int(year), int(month), int(day))

    @staticmethod
    def add_day(date, days):
        return date + timedelta(days=days)
