"""options"""
import argparse

parser = argparse.ArgumentParser(description='Event Connector')
parser.add_argument('--starting', help='Specify start of event time range in ISO-8601 format', required=False)
parser.add_argument('--ending', help='Specify end of event time range in ISO-8601 format', required=False)
parser.add_argument('--auth',
                    help='Specify a file containing CloudPassage Halo API keys - Key ID and Key secret pairs (up to 5)',
                    required=True)
parser.add_argument('--batchsize', help='Specify a limit for page numbers, after which we use since', required=False)
parser.add_argument('--configdir', help='Specify directory for configration files (saved timestamps)', required=False)
parser.add_argument('--jsonfile', help='Write events in raw JSON format to file with given filename', required=False)
parser.add_argument('--event_type', help='Filter retrieved events based on event type', required=False)


class Options(object):
    """options class"""

    def __new__(cls):
        args = vars(parser.parse_args())
        return args
