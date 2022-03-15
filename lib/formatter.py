"""Formatter class definition."""
from lib.config_helper import ConfigHelper
from datetime import datetime
from lib.options import Options


class Formatter(object):
    """Instantiate Formatter class.

    Args:
        options(lib.Options): Optional.

    Attributes:
        options(lib.Options): Instance variable. Set from init argument.
        product_version(str): Instance variable. Version of connector tool.
        datetime_format(None): Class variable. This is overridden as-needed by
            sub-classes.
    """

    datetime_format = None

    def __init__(self, options=None):
        self.options = options or Options()
        self.product_version = ConfigHelper.get_product_version()

    def format_event(self, event):
        """This method is implemented in sub-classes."""
        raise NotImplementedError

    @classmethod
    def format_timestamp(cls, dt):
        """Return a formatted time stamp.

        In the parent ``Formatter`` class, this returns ``None`` because no
        datetime format is set.  Subclasses may set ``self.datetime_format``
        to format timestamps for different output requirements.

        Args:
            fmt(str): Format which describes the desired output format for
                time stamp

        Returns:
            str: Formatted ``dt``.
        """
        if cls.datetime_format is None:
            return None
        return dt.strftime(cls.datetime_format)

    @classmethod
    def halo_timestamp_to_datetime(cls, halo_timestamp):
        """Return datetime object for Halo event timestamp."""
        return datetime.strptime(halo_timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')

    def format_events(self, events):
        """Iterate over format_event."""
        formatted_events = []
        for event in events:
            formatted_events.append(self.format_event(event))
        return formatted_events
