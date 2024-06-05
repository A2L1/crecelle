import os
import subprocess

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

    command = f"nmap -sV --script vulners -iL {temp_file} -oX {output_path}"        
    result = subprocess.run(command,stderr=subprocess.PIPE, shell=True, executable="/bin/bash")

    os.remove(temp_file)

    if result.stderr:
        print(f"{RED}Erreur lors de l'execution: {COLOR_OFF}")
        print(result.stderr)
    else:
        print(f"{GREEN}Nmap vulners script done{COLOR_OFF}")
        print(f"{BLUE}le fichier existe: {output_path}{COLOR_OFF}")

def launch_nmap_scan_input(target_ip="",directory_save_path="",scan_name=""):

    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    COLOR_OFF = "\033[0m"

    print(f"{BLUE}Execution nmap{COLOR_OFF}")

    scan_path = f"{directory_save_path}/{scan_name}/nmap"
    output_path = f"{scan_path}/{scan_name}-nmap.xml"

    command = f"nmap -sV --script vulners {target_ip} -oX {output_path}"        
    result = subprocess.run(command,stderr=subprocess.PIPE, shell=True, executable="/bin/bash")

    if result.stderr:
        print(f"{RED}Erreur lors de l'execution: {COLOR_OFF}")
        print(result.stderr)
    else:
        print(f"{GREEN}Nmap vulners script done{COLOR_OFF}")
        print(f"{BLUE}le fichier existe: {output_path}{COLOR_OFF}")

    print('test')