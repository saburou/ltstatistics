# -*- coding: utf-8 -*-
from core.analyzer import Analyzer
from entity.stream import Stream
from entity.st_view import StView
from entity.st_total_view import StTotalView
from entity.st_comment import StComment
from datetime import datetime
import logging


class ViewAnalyzer(Analyzer):
    """
    Analysis stream viewing information.
    """
    def analyze(self, data):
        currentdate = datetime.now()
        # Regist individual stream view.
        total = 0
        for d in data:
            if not isinstance(d, Stream):
                continue
            # Regist viewing.
            view = StView(d.get_id(), currentdate, d.get_viewing())
            if view.count() > 0:
                view.update()
            else:
                view.regist()
            total += d.get_viewing()
            # Regist comments.
            comment = StComment(d.get_id(), currentdate, d.get_comments())
            if comment.count() > 0:
                comment.update()
            else:
                comment.regist()
        # Regist total stream view.
        totalview = StTotalView(currentdate, total)
        totalview.regist()
