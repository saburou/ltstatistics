# -*- coding: utf-8 -*-
from model.models import Stream
from datetime import datetime


class StreamParser:

    @staticmethod
    def parse(jsondata):
        if jsondata is None:
            return []

        result = []
        for stream in jsondata:
            result.append(Stream(id=stream["id"], title=stream["title"], author=stream["author"],
                                 startdate=datetime.strptime(stream["created"], '%a, %d %b %Y %H:%M:%S %Z'),
                                 viewing=stream["viewing"], comments=stream["comments"]))
        return result
