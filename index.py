#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import get, run, response
import json
from model.models import StTotalView
from common.validator import DayValidator
from common.message import Message
from common.date import DateUtils
from core.session import DBSessionFactory

CONTENT_TYPE = 'application/json'


@get('/api/totalview/day/<date>')
def daytotalview(date):
    """
    指定年月日の統計視聴情報を返します。
    :param date: 対象日
    :return: 統計視聴情報
    """
    if not DayValidator().isvalid(date):
        return Message.error(Message.ID_BAD_REQUEST, Message.TEXT_INVALID_DATE)

    response.content_type = CONTENT_TYPE

    startdate = DateUtils.parse(date)
    enddate = DateUtils.add_day(startdate, 1)

    session = DBSessionFactory.create()
    data = StTotalView().select(target_startdate='%s-%s-%s' % (startdate.year, startdate.month, startdate.day),
                                target_enddate='%s-%s-%s' % (enddate.year, enddate.month, enddate.day),
                                session=session)

    result = []
    for d in data:
        result.append({'date': d.date.strftime("%Y/%m/%d %H:%M:%S"), 'amount': d.amount})

    session.close()

    return json.dumps({'unit': 'day', 'view': result}).replace("\\", "")


if __name__ == "__main__":
    run(host='localhost', port=8080)
