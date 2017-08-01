# -*- coding: utf-8 -*-
import json


class Message:
    """
    Define JSON messages and template.
    """

    ID_BAD_REQUEST = 500

    TEXT_INVALID_DATE = "Request had invalid date format."

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
