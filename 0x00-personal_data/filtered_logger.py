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
    pattern = '|'.join(map(re.escape, fields))
    return re.sub(pattern, redaction, message)
