# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Analyzer(metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def analyze(self, data):
        """
        Analyze data.
        :param data: target data. 
        :return: data analyzed.
        """
        raise NotImplementedError
    