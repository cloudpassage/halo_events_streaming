# HALO EVENTS STREAMING TOOL v1.0

### About the tool:
The major goal of halo events streaming tool is to retrieve all/specific  types of  halo events within a specific user defined time range
into a local JSON file format.

### Installing and running Halo Events Streaming tool as a native python script:
1. Install Python 3.6 or newer (https://www.python.org/downloads)

2. Check out `halo_events_streaming` repository into location from your choice (i.e., /opt/cloudpassage):
```
mkdir -p /opt/cloudpassage
cd /opt/cloudpassage
git clone https://github.com/cloudpassage/halo_events_streaming.git
```

3. Install the required python modules/packages:
```
cd halo_events_streaming
pip install -r requirements.txt
```

4. Configure Halo authentication information for the tool:
* In your CloudPassage portal account, generate an auditor (read-only) API key.
* Place the API key and secret, pipe-separated, in a file named `halo.auth` and save it into
`halo_events_streaming/configs/halo.auth`. The file will contain one line, which looks like this: 
`haloapikey|haloapisecret`, replacing `haloapikey` with the key ID for your Halo API key, 
and replacing `haloapisecret` with your API key's secret.

5. Run halo events streaming tool:
```
python halo_events.py --auth=halo.auth -- --starting=YYYY-MM-DD --ending=YYYY-MM-DD --configdir=./configs --jsonfile=/var/log/halo-events.json
```

* Example:

`python halo_events.py --auth=/opt/cloudpassage/halo_events_streaming/configs/halo.auth --starting=2022-03-14 --ending=2022-03-16 --configdir=/opt/cloudpassage/halo_events_streaming/configs --jsonfile=/var/log/halo-events.json`

* Monitor the json files `/var/log/halo-events.json` and `/var/log/halo-events-desc.json` to see events from your Halo account.
* You can filter HALO events by setting event type to any of the supported event types illustrated in [EVENT TYPES](SUPPORTED_EVENT_TYPES.md) document.

### Implementation Notes:
__CLI Options:__
```
usage: halo_events.py   [-h] 
                        [--starting STARTING] 
                        [--ending ENDING] 
                        [--auth AUTH]
                        [--batchsize BATCHSIZE]
                        [--configdir CONFIGDIR] 
                        [--jsonfile JSONFILE]
                        [--event_type EVENT_TYPE]

HALO Events Streaming tool

optional arguments:
  -h, --help            show this help message and exit
  --starting STARTING   Specify start of event time range in ISO-8601 format
  --ending ENDING       Specify end of event time range in ISO-8601 format
  --auth AUTH           Specify a file containing CloudPassage Halo API keys - Key ID and Key secret pairs
  --batchsize BATCHSIZE Specify a limit for page numbers, after which we use since
  --configdir CONFIGDIR Specify directory for configration files (saved timestamps)
  --jsonfile JSONFILE   Write events in raw JSON format to file with given filename
  --event_type          Filter retrieved events based on event type (i.e. --event_type=lids_rule_failed,sca_rule_failed)
```
