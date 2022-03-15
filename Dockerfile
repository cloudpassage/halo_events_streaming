FROM docker.io/halotools/python-sdk:ubuntu-18.04_sdk-latest_py-3.6

MAINTAINER toolbox@cloudpassage.com

RUN mkdir /app

COPY ./ /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "halo_events.py"]