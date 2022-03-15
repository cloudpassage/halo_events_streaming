# HALO Events Streaming v1.0

### About the tool
HALO Events Streaming tool retrieves Halo events within a specific user defined time range into a local JSON file format.

* In the examples below, we are trying to retrieve events starting on March 1st, 2022 and ending by March 15th, 2022.  (Halo
   only retains events for 90 days).

First, we check out halo_events_streaming repository into any location from your choice (i.e., /opt/cloudpassage):

* `mkdir -p /opt/cloudpassage`
* `cd /opt/cloudpassage`
* `git clone https://github.com/cloudpassage/halo_events_streaming.git`

Next, install the required python packages:
* `cd halo_events_streaming`
* `pip install -r requirements.txt`

Next, configure Halo authentication information for the tool:

* In your CloudPassage portal account, generate an auditor (read-only) API key.
* Place the API key and secret, pipe-separated, in a file at
`/opt/cloudpassage/halo_events_streaming/configs/halo.auth`.  The file will contain one
line, which looks like this: `haloapikey|haloapisecret`, replacing `haloapikey`
with the key ID for your Halo API key, and replacing `haloapisecret` with your
API key's secret.

Next, run the Halo Events Streaming:

`py halo_events.py --auth=/opt/cloudpassage/halo_events_streaming/configs/halo.auth --starting=2022-03-01 --ending=2022-03-15 --configdir=/opt/cloudpassage/halo_events_streaming/configs --event_type=fim_target_integrity_changed --jsonfile=/var/log/halo-events.json`

Monitor the `/var/log/halo-events.json` file to see events from your Halo account.


### Implementation Notes

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

HALO Events Streaming

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

### Halo Events Streaming on Linux

* Install Python 3.6 or newer (https://www.python.org/downloads)

* Once Python is installed, install the necessary Python modules:

```
pip install -r requirements.txt
```

* Download the Halo Events Streaming (https://github.com/cloudpassage/halo_events_streaming)

6. Create the `halo.auth` file

7. Run the halo events streaming (must specify a starting cli parameter)

```
python halo_events.py --auth=halo.auth --starting=YYYY-MM-DD --ending=YYYY-MM-DD
```

### Halo Events Streaming on Windows

* Install Python 3.6 or newer (https://www.python.org/downloads/windows/)

* Add python installation folder to system PATH environmental variable or
create PYTHONPATH environment variable and set installation folder location as
follows (C:\Python36\lib;C:\Python36)

* Once Python is installed, install the necessary Python modules

```
python -m pip install -r requirements.txt
```

* Download the Halo Events Streaming (https://github.com/cloudpassage/halo_events_streaming)

* Create the halo.auth file

* Run the Halo Events Streaming (currently must specify a starting cli parameter)

```
python halo_events.py --auth=halo.auth --starting=YYYY-MM-DD --ending=YYYY-MM-DD
```


### Halo Events Streaming as Docker Container

#### Requirements:
  * Docker engine (https://docs.docker.com/engine/install/)
  * A Halo account (with auditor role)
  * Clone Halo Events Streaming repository

```
git clone https://github.com/cloudpassage/halo_events_streaming.git
```

  * Navigate to the root directory of Halo Events Streaming repository
  * Place the Halo API key ID and secret, pipe-separated, in a file at `/configs/halo.auth`.  The file will contain one
    line, which looks like this: `haloapikey|haloapisecret`, replacing `haloapikey` with the key ID for your Halo API key, and replacing `haloapisecret` with your
    API key's secret.

  * build the halo events streaming docker image:
```
sudo docker build -t Halo_Events_Streaming .
```

  * Run the docker container:
```
sudo docker run -it --rm \
	-v /LOCAL/PATH/TO/LOGS:/var/log \
	-v /dev/log:/dev/log \
	-v /LOCAL/PATH/TO/CONFIGS:/app/configs \
	Halo_Events_Streaming \
	--auth=/app/configs/halo.auth \
	--configdir=/app/configs \
	--starting=YYYY-MM-DD \
	--ending=YYYY-MM-DD \
	--event_type=SUPPORTED_EVENT_TYPE \
	--jsonfile=/var/log/halo-events.json \
```
 
#### Examples:

##### Retrieving HALO Events into json file
```
$ sudo docker run -it --rm \
	-v /var/log:/var/log \
	-v /dev/log:/dev/log \
	-v /home/ubuntu/halo_events_streaming/configs:/app/configs \
	halo_events_streaming \
	--auth=/app/configs/halo.auth \
	--configdir=/app/configs \
	--starting=2022-03-01 \
	--ending=2022-03-15 \
	--event_type=lids_rule_failed \
	--jsonfile=/var/log/halo-events.json
```
  * Monitor `/var/log/halo-events.json` files to see retrieved events from your HALO account.
  * You can filter HALO events by setting event type to any of the supported event types illustrated in [EVENT TYPES](SUPPORTED_EVENT_TYPES.md) document.