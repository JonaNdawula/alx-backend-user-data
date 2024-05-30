#!/usr/bin/env python3
"""
This module contains functions
that return the log message
obfuscated
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    Returns the log message with certain fields
    obfuscated
    """
    for field in fields:
        message = re.sub(f"{field}=[^{separator}]*",
                         f"{field}={redaction}", message)
    return message
