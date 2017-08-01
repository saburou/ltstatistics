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
    Response total viewings information in target date.
    :param date: target date (format: yyyy-mm-dd)
    :return: total viewings
    """
    if not DayValidator().isvalid(date):
        return Message.error(Message.ID_BAD_REQUEST, Message.INVALID_DATE)

    response.content_type = CONTENT_TYPE

    startdate = DateUtils.parse(date)
    enddate = DateUtils.add_day(startdate, 1)

    session = DBSessionFactory.create()
    data = StTotalView().select(target_startdate=startdate, target_enddate=enddate, session=session)

    result = []
    for d in data:
        result.append({'date': d.date.strftime("%Y/%m/%d %H:%M:%S"), 'amount': d.amount})

    session.close()

    return json.dumps({'unit': 'day', 'view': result}).replace("\\", "")


@get('/api/totalview/month/<date>')
def monthtotalview(date):
    response.status = Message.ID_NOT_IMPLEMENTED
    return Message.error(Message.ID_NOT_IMPLEMENTED, Message.NOT_IMPLEMENTED)


@get('/api/totalview/year/<date>')
def monthtotalview(date):
    response.status = Message.ID_NOT_IMPLEMENTED
    return Message.error(Message.ID_NOT_IMPLEMENTED, Message.NOT_IMPLEMENTED)


if __name__ == "__main__":
    run(host='localhost', port=8080)
