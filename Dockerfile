FROM kalilinux/kali-last-release

RUN apt-get update -y && apt-get upgrade -y && apt-get -y install subfinder python3 dnsrecon nmap git xsltproc 

RUN apt-get install -y exploitdb exploitdb-papers exploitdb-bin-sploits

WORKDIR /crecerelle-project

COPY crecerelle-project/ .

WORKDIR /crecerelle-project

RUN setcap cap_net_raw+eip $(which nmap)

RUN git clone https://github.com/ernw/nmap-parse-output.git

CMD /bin/bash

# CMD python3 main.py
