"""Json and key-value formatter"""
import json
from lib.formatter import Formatter


class FormatJson(Formatter):
    def format_event(self, event):
        """Return Halo event, formatted as a json string."""
        formatted_event = "%s\n" % json.dumps(event)
        return formatted_event


class FormatKv(Formatter):
    def format_event(self, event):
        """Return Halo event, formatted as a key-value string"""
        formatted_event = ""
        for key, value in event.items():
            formatted_event += "%s=\"%s\" " % (key, value)
        formatted_event += "\n"
        return formatted_event
