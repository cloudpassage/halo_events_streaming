"""validator"""
import datetime
import platform
import dateutil.parser
import pytz
import lib.settings as settings


def validate_time(date):
    """validate time"""
    date = date.replace('+', ':')
    try:
        dateutil.parser.parse(date)
    except:
        raise ValueError(date + " is not in iso8601 time format")


def validate_time_range(date):
    """validate time range"""
    date = date.replace('+', ':')
    date_parsed = dateutil.parser.parse(date)
    if date_parsed.tzinfo is None:
        date_parsed = pytz.utc.localize(date_parsed)
    time_range = (datetime.datetime.utcnow().replace(tzinfo=pytz.utc) - datetime.timedelta(
        days=settings.historical_limit()))  # NOQA

    if date_parsed < time_range:
        raise ValueError(date + " is out of range")


def validate_start_end_time_range(start_date, end_date):
    """validate time range"""
    start_date = start_date.replace('+', ':')
    start_date_parsed = dateutil.parser.parse(start_date)
    if start_date_parsed.tzinfo is None:
        start_date_parsed = pytz.utc.localize(start_date_parsed)
    end_date = end_date.replace('+', ':')
    end_date_parsed = dateutil.parser.parse(end_date)
    if end_date_parsed.tzinfo is None:
        end_date_parsed = pytz.utc.localize(end_date_parsed)
    if end_date_parsed < start_date_parsed:
        raise ValueError("["+end_date+"] must be after the start date ["+start_date+"]")


def batchsize(page):
    """validate batchsize"""
    try:
        int(page)
    except:
        raise ValueError(page + " is not an integer")
    if int(page) > settings.pagination_limit():
        raise ValueError("you have exceeded the batchsize limitation")


def starting(date):
    """validate starting"""
    validate_time(date)
    validate_time_range(date)


def ending(start_date, end_date):
    """validate ending"""
    validate_time(end_date)
    validate_start_end_time_range(start_date, end_date)


def operating_system():
    """determine operating_system"""
    if platform.system() == 'Windows':
        return "windows"
    return "linux"