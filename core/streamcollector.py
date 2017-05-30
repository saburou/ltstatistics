# -*- coding: utf-8 -*-
import json
from core.requester import APIRequester
from core.parser import StreamParser
from core.viewanalyzer import ViewAnalyzer


class StreamCollector:
    """
    Get live-stream data from target uri, then regist their statictics.
    """
    HOST = 'http://livetube.cc/index.live.json'

    @staticmethod
    def request():
        """
        Request live-stream list from target uri. 
        :return:  Streams
        """
        requestor = APIRequester(StreamCollector.HOST)
        j = json.loads(requestor.request())

        if j is None:
            return

        return StreamParser.parse(j)
# Request stream information.
streams = StreamCollector.request()

# Regist stream information.
if streams is None:
    exit()

for s in streams:
    if s is None:
        continue
    if s.count() == 0:
        s.regist()

# Analyze stream information.
analyzer = ViewAnalyzer()
analyzer.analyze(streams)
