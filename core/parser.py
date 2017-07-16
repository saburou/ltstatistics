# -*- coding: utf-8 -*-
import json
from model.models import Stream


class StreamParser:

    @staticmethod
    def parse(jsondata):
        if jsondata is None:
            return []

        result = []
        for stream in jsondata:
            result.append(Stream(id=stream["id"], title=stream["title"], author=stream["author"], startdate=stream["created"], viewing=stream["viewing"], comments=stream["comments"]))
        return result
