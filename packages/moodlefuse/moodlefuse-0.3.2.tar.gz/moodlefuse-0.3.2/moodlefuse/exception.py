#!/usr/bin/env python
# encoding: utf-8

"""Class to handle Exceptions relating to MoodleFUSE actions
"""

from functools import wraps

from moodlefuse.core import config


class MoodleFuseException(Exception):
    def __init__(self, debug_info):
        _EXCEPTION_REASON = "ERROR ENCOUNTERED: MoodleFUSE has encountered an error."
        self.message = _EXCEPTION_REASON + debug_info

    def __str__(self):
        return self.message


def throws_moodlefuse_error(moodlefuse_error):
    def inner(f):
        def wrapped(*args):
            try:
                return f(*args)
            except Exception, e:
                if config['DEBUG'] is False:
                    raise moodlefuse_error()
                else:
                    raise e
        return wraps(f)(wrapped)
    return inner
