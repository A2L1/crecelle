FROM kalilinux/kali-last-release

RUN apt-get update -y && apt-get upgrade -y && apt-get -y install subfinder python3 dnsrecon

WORKDIR /crecerelle-project

COPY crecerelle-project/ .

WORKDIR /crecerelle-project

# CMD /bin/bash

CMD python3 main.py
