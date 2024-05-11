FROM kalilinux/kali-last-release

RUN apt-get update -y && apt-get upgrade -y && apt-get -y install subfinder python3 dnsrecon

WORKDIR /crecelle-project

COPY crecelle-project/ .

WORKDIR /crecelle-project/utils

# CMD /bin/bash

CMD python3 ../main.py
