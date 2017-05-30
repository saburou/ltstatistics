# -*- coding: utf-8 -*-
import string
from datetime import datetime
from common.validator.validator import BaseValidator


class DayValidator(BaseValidator):
    """
    Validate date in format "%Y-%m-%d".
    """

    def isvalid(self, target):
        if not isinstance(target, str):
            return False

        try:
            a = datetime.strptime(target, "%Y-%m-%d")
        except ValueError as e:
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
            a = datetime.strptime(target, "%Y-%m")
        except ValueError as e:
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
            a = datetime.strptime(target, "%Y")
        except ValueError as e:
            return False

        return True
