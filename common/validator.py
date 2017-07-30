# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from datetime import datetime


class BaseValidator(metaclass=ABCMeta):
    """
    Base class for implements validation.
    """
    def __init__(self):
        return

    @abstractmethod
    def isvalid(self, target):
        """
        Validate object in individual implementation.
        :param target: target object
        :return: object is valid.
        """
        raise NotImplementedError


class DayValidator(BaseValidator):
    """
    Validate date in format "%Y-%m-%d".
    """
    def isvalid(self, target):
        if not isinstance(target, str):
            return False

        try:
            datetime.strptime(target, "%Y-%m-%d")
        except ValueError:
            return False

        return True


class MonthValidator(BaseValidator):
    """
    Validate month in format "%Y-%m".
    """
    def isvalid(self, target):
        if not isinstance(target, str):
            return False

        try:
            datetime.strptime(target, "%Y-%m")
        except ValueError:
            return False

        return True


class YearValidator(BaseValidator):
    """
    Validate year in format "%Y".
    """
    def isvalid(self, target):
        if not isinstance(target, str):
            return False

        try:
            datetime.strptime(target, "%Y")
        except ValueError:
            return False

        return True
