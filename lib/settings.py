"""Halo Events Streaming settings"""
import datetime

import pytz


def per_page():
    """max events return per page"""
    return 100


def pagination_limit():
    """max page return"""
    return 50


def historical_limit():
    """max days"""
    return 90


def event_type():
    """all events"""
    return ""


def ending_date():
    """get current datetime"""
    current_datetime = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
    return current_datetime
