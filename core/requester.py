# -*- coding: utf-8 -*-
import urllib.request as r


class APIRequester:

    def __init__(self, uri):
        self._uri = uri

    def request(self):
        req = r.Request(self._uri)
        result = r.urlopen(req)
        if result is None:
            return None

        if result.status != 200:
            return None

        return result.read()
