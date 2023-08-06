# Copyright (c) Qotto, 2021

"""
Messaging errors
"""

__all__ = [
    'MessagingError',
]


class MessagingError(Exception):
    """
    Base Error class of all messaging API
    """


class EventyAppInterrupted(MessagingError):
    """
    Eventy app interrupted
    """


class AppCancelled(EventyAppInterrupted):
    """
    Eventy App is cancelled
    """


class ParentThreadDied(EventyAppInterrupted):
    """
    Eventy App is cancelled
    """


class BatchFailed(EventyAppInterrupted):
    """
    Batch processing failed
    """
