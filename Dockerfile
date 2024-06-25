FROM kalilinux/kali-last-release

RUN apt-get update -y && apt-get upgrade -y && apt-get -y install subfinder python3 dnsrecon nmap

RUN apt-get install -y exploitdb exploitdb-papers exploitdb-bin-sploits

RUN apt install -y weasyprint

RUN wget https://bootstrap.pypa.io/get-pip.py

RUN python3 ./get-pip.py

RUN pip install matplotlib pandas seaborn

WORKDIR /crecerelle-project

COPY crecerelle-project/ .

RUN setcap cap_net_raw+eip $(which nmap)

# CMD /bin/bash

CMD python3 main.py
