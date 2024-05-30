#!/usr/bin/env python3
"""
This module contains functions
that return the log message
obfuscated
"""
import re
import logging


def filter_datum(
    fields: list, redaction: str, message: str, separator: str
) -> str:
    """
    Returns the log message with certain fields
    obfuscated
    """
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]*",
                         f"{field}={redaction}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        """
        initializer
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Function to format
        """
        o_msg = super().format(record)
        return filter_datum(self.fields, self.REDACTION, o_msg, self.SEPARATOR)
