# -*- coding: utf-8 -*-
import json


class Message:
    """
    Define JSON messages and template.
    """

    ID_BAD_REQUEST = 500
    ID_NOT_IMPLEMENTED = 501
    ID_SERVICE_UNAVAILABLE = 503

    INVALID_DATE = "Request had invalid date format."
    NOT_IMPLEMENTED = "Request API is not implemented."
    SERVICE_UNAVAILABLE = "Request API is unavailable."

    @staticmethod
    def info(message_id, message):
        """
        Create info message in JSON. 
        :param message_id: message id
        :param message:  text embeded into message.
        :return: JSON in term of info.
        """
        return json.dumps({"info": {"id": message_id, "message": message}})

    @staticmethod
    def error(message_id, message):
        """
        Create error message in JSON.
        :param message_id:  message id
        :param message: text embeded into message.
        :return: JSON in term of error.
        """
        return json.dumps({"error": {"id": message_id, "message": message}})
