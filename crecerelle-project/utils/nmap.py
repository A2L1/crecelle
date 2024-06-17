import os
import subprocess
import json
import xml.etree.ElementTree as ET

def launch_nmap_scan_list(list_ip_subdomain="",directory_save_path="",scan_name=""):

    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    COLOR_OFF = "\033[0m"

    print(f"{BLUE}Execution nmap{COLOR_OFF}") 
    list_ip = list(list_ip_subdomain.keys())

    temp_file = "/tmp/tmp_list_ip_scan.txt"

    with open(temp_file,"w") as file:
        for ip in list_ip:
            file.write(f'{ip}\n')

    scan_path = f"{directory_save_path}/{scan_name}/nmap"
    output_path = f"{scan_path}/{scan_name}-nmap.xml"

    command = f"nmap -sS -sV --script vulners -iL {temp_file} -oX {output_path}"        
    result = subprocess.run(command,stderr=subprocess.PIPE, shell=True, executable="/bin/bash")

    os.remove(temp_file)

    if result.stderr:
        print(f"{RED}Erreur lors de l'execution: {COLOR_OFF}")
        print(result.stderr)
    else:
        print(f"{GREEN}Nmap vulners script done{COLOR_OFF}")
        print(f"{BLUE}le fichier existe: {output_path}{COLOR_OFF}")

    convert_output(xml_file=output_path,scan_name=scan_name,scan_path=scan_path)

    
def launch_nmap_scan_input(target_ip="",directory_save_path="",scan_name=""):

    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    COLOR_OFF = "\033[0m"

    print(f"{BLUE}Execution nmap{COLOR_OFF}")

    scan_path = f"{directory_save_path}/{scan_name}/nmap"
    output_path = f"{scan_path}/{scan_name}-f-nmap.xml"

    command = f"nmap -sS -sV --script vulners {target_ip} -oX {output_path}"        
    result = subprocess.run(command,stderr=subprocess.PIPE, shell=True, executable="/bin/bash")

    if result.stderr:
        print(f"{RED}Erreur lors de l'execution: {COLOR_OFF}")
        print(result.stderr)
    else:
        print(f"{GREEN}Nmap vulners script done{COLOR_OFF}")
        print(f"{BLUE}le fichier existe: {output_path}{COLOR_OFF}")

    convert_output(xml_file=output_path,scan_name=scan_name,scan_path=scan_path)

def convert_output(xml_file,scan_name,scan_path):

    print(xml_file)

    tree = ET.parse(xml_file)
    root = tree.getroot()

    hosts_info = {}

    for host in root.findall('host'):
        print(host)
        addr_element = host.find('address')
        if addr_element is not None:
            ip_address = addr_element.get('addr')
            hosts_info[ip_address] = {'ports': []}
            
            for port in host.findall('ports/port'):
                port_id = port.get('portid')
                protocol = port.get('protocol')
                state = port.find('state').get('state')
                service_info = port.find('service')
                
                port_data = {
                    'port_id': port_id,
                    'protocol': protocol,
                    'state': state,
                }

                service_data = {}
                if service_info is not None:
                    for key in ['name', 'product', 'version']:
                        service_data[key] = service_info.get(key, 'None')

                vulnerabilities = []
                for script in port.findall('script'):
                    if script.get('id') == 'vulners':
                        for table in script.findall('table'):
                            for sub_table in table.findall('table'):
                                vuln_info = {}
                                for elem in sub_table.findall('elem'):
                                    key = elem.get('key')
                                    vuln_info[key] = elem.text
                                if vuln_info:
                                    vulnerabilities.append(vuln_info)

                port_info = {
                    'port': port_data,
                    'service': service_data,
                    'vulnerabilities': vulnerabilities
                }
                
                hosts_info[ip_address]['ports'].append(port_info)

    print(hosts_info)

    with open(f"{scan_path}/{scan_name}-nmap.json", 'w') as f:
        json.dump(hosts_info, f, indent=4)