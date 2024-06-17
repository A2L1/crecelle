FROM kalilinux/kali-last-release

RUN apt-get update -y && apt-get upgrade -y && apt-get -y install subfinder python3 dnsrecon nmap git

RUN apt-get install -y exploitdb exploitdb-papers exploitdb-bin-sploits

WORKDIR /crecerelle-project

COPY crecerelle-project/ .

RUN setcap cap_net_raw+eip $(which nmap)

# RUN git clone https://github.com/ernw/nmap-parse-output.git

# RUN wget https://bootstrap.pypa.io/get-pip.py

# RUN python3 ./get-pip.py

# RUN pip install lxml

# CMD /bin/bash

CMD python3 main.py
