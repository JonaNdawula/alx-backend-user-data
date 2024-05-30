#!/usr/bin/env python3
"""
This module contains functions
that returns the log message
obfuscated
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    Returns the log message with certain fields
    obfuscated
    """
    return re.sub(separator.join(fields), redaction, message)
