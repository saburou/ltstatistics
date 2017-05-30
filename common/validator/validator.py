# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class BaseValidator(metaclass=ABCMeta):
    """
    Base class for implements validation.
    """
    def __init__(self):
        return;

    @abstractmethod
    def isvalid(self, target):
        """
        Validate object in individual implementation.
        :param target: target object
        :return: object is valid.
        """
        raise NotImplementedError
