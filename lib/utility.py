"""Utility class"""
import os
import signal
from lib.options import Options
import lib.validate as validate
from lib.jsonkv import FormatJson
import lib.settings as settings
import sys
import importlib

importlib.reload(sys)


class Utility(object):
    """Utility class"""

    def __init__(self, options=None):
        self.options = options or Options()
        self.json_formatter = FormatJson(options)

    def rename(self, original, new):
        """rename"""
        os.rename(original, new)

    def interrupt_handler(self, signum, frame):
        """interruptHandler"""
        print("Beginning shutdown...")

    def init_worker(self):
        """init_worker"""
        signal.signal(signal.SIGINT, self.interrupt_handler)

    def write_output(self, filename, formatted_events):
        """write output"""
        with open(filename, 'a') as outputfile:
            for formatted_event in formatted_events:
                outputfile.write("%s\n" % formatted_event.encode('utf-8'))
        outputfile.close()

    def output_events(self, batched):
        """output events"""
        if self.options["jsonfile"] is not None:
            self.write_output(self.options["jsonfile"],
                              self.json_formatter.format_events(batched))
        else:
            pass

    def parse_auth(self):
        """parse auth file"""
        auth_keys = []
        with open(self.options['auth'], 'r') as outputfile:
            auth_file = map(str.rstrip, outputfile)
            for line in auth_file:
                key, secret = line.split("|")
                auth_keys.append({"key_id": key, "secret_key": secret})
        return auth_keys

    def parse_pagination_limit(self):
        """determine pagination_limit"""
        if self.options['batchsize'] is None:
            return settings.pagination_limit()
        validate.batchsize(self.options['batchsize'])
        return int(self.options['batchsize'])

    def check_starting(self):
        """determine starting date"""
        if self.options["starting"] and self.options["configdir"] is None:
            validate.starting(self.options["starting"])
            return self.options["starting"]
        elif self.options["starting"] is None and self.options["configdir"]:
            try:
                return self.parse_configdir_file()[0]["end_date"]
            except:
                return None
        else:
            try:
                return self.parse_configdir_file()[0]["end_date"]
            except:
                return self.options["starting"]

    def check_ending(self):
        """determine ending date"""
        if self.options["ending"]:
            validate.ending(self.options["ending"], self.options["ending"])
            return self.options["ending"]
        else:
            return settings.ending_date()

    def parse_configdir(self):
        """determine config directory"""
        if self.options["configdir"] is None:
            return os.path.join(os.path.dirname(__file__),
                                os.pardir, 'configs')
        return self.options["configdir"]

    def parse_configdir_file(self):
        """determine configdir date"""
        key_date = []
        files = os.listdir(self.options["configdir"])
        if files:
            for onefile in files:
                if not onefile.startswith('.'):
                    if "_" in onefile:
                        key, end_date = onefile.split("_")
                        validate.starting(end_date)
                        key_date.append({"key_id": key, "end_date": end_date})
        else:
            raise ValueError("Please use --starting to specify starting date")
        return key_date

    def parse_event_type(self):
        """determine event type"""
        if self.options['event_type'] is None:
            return settings.event_type()
        return self.options['event_type']

    def updated_hash(self):
        """updated hash"""
        self.options["api_keys"] = self.parse_auth()
        self.options["batchsize"] = self.parse_pagination_limit()
        self.options["configdir"] = self.parse_configdir()
        self.options["starting"] = self.check_starting()
        self.options["ending"] = self.check_ending()
        self.options["event_type"] = self.parse_event_type()
        return self.options
