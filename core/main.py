# -*- coding: utf-8 -*-
import json
from core.requester import APIRequester
from core.parser import StreamParser
from core.register import ViewRegister, StreamRegister
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.models import Stream, StTotalView, StView, StComment


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


if __name__ == "__main__":
    # Request stream information.
    streams = StreamCollector.request()

    # Regist stream information.
    if streams is None:
        exit()
    stream_register = StreamRegister()
    stream_register.regist(streams)

    # Regist viewing information.
    view_register = ViewRegister()
    view_register.regist(streams)
