"""HALO Events Streaming"""
from lib.settings import event_type
from lib.utility import Utility
from lib.event import Event


def main():
    """Main function for retrieving events"""
    utility = Utility()
    args = utility.updated_hash()
    if args["starting"] is not None:
        for i in args["api_keys"]:
            event = Event(i['key_id'], i['secret_key'])
            event.retrieve_events()
            event.sort_events()


if __name__ == "__main__":
    main()
