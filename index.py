#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import get, run, response
import json
from entity.st_total_view import StTotalView
from common.validator.datevalidator import *
from common.message.message import Message

CONTENT_TYPE = 'application/json'

@get('/api/totalview/day/<date>')
def daytotal(date):
    """
    指定年月日の統計視聴情報を返します。
    :param date: 対象日
    :return: 統計視聴情報 
    """
    if not DayValidator().isvalid(date):
        return Message.error(Message.ID_BAD_REQUEST, Message.TEXT_INVALID_DATE)

    dateparams = date.split("-")
    year = dateparams[0]
    month = dateparams[1]
    day = dateparams[2]

    response.content_type = CONTENT_TYPE
    data = StTotalView().findday('%s-%s-%s' % (year, month, day), '%s-%s-%s' % (year, month, str(int(day)+1)))
    result = []
    for d in data:
        result.append({'measuredate': d.get_measuredate(), 'amount': d.get_amount()})
    return json.dumps({'term': 'day', 'totalview': result}).replace("\\", "")


@get('/api/totalview/month/<date>')
def monthtotal(date):
    """
    指定年月の統計視聴情報を返します。 
    :param date: 対象月
    :return: 統計視聴情報 
    """
    if not MonthValidator().isvalid(date):
        return Message.error(Message.ID_BAD_REQUEST, Message.TEXT_INVALID_DATE)

    dateparams = date.split("-")
    year = dateparams[0]
    month = dateparams[1]

    response.content_type = CONTENT_TYPE
    data = StTotalView().findmonth('%s-%s' % (year, month), '%s-%s' % (year, str(int(month)+1)))
    result = []
    for d in data:
        result.append({'measuredate': d.get_measuredate(), 'amount': d.get_amount()})
    return json.dumps({'term': 'month', 'totalview': result}).replace("\\", "")


@get('/api/totalview/year/<date>')
def yeartotal(date):
    """
    指定年の統計視聴情報を返します。
    :param year: 対象年
    :return: 統計視聴情報 
    """
    if not YearValidator().isvalid(date):
        return Message.error(Message.ID_BAD_REQUEST, Message.TEXT_INVALID_DATE)

    dateparams = date.split("-")
    year = dateparams[0]

    response.content_type = CONTENT_TYPE
    data = StTotalView().findyear('%s' % year, '%s' % str(int(year)+1))
    result = []
    for d in data:
        result.append({'measuredate': d.get_measuredate(), 'amount': d.get_amount()})
    return json.dumps({'term': 'year', 'totalview': result}).replace("\\", "")

run(host='localhost', port=8080)
