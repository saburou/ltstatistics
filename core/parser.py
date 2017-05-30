# -*- coding: utf-8 -*-
import json
from entity.stream import Stream


class StreamParser:

    @staticmethod
    def parse(jsondata):
        if jsondata is None:
            return []

        result = []
        for stream in jsondata:
            result.append(Stream(stream["id"], stream["title"], stream["author"], stream["created"], stream["viewing"], stream["view"], stream["comments"]))
        return result
