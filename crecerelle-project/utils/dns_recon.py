import csv
import subprocess
import os
import json

def merge_ip_into_single_file(dir_path):
    liste_file_to_merge = os.listdir(dir_path)
    # print(liste_file_to_merge)
    liste_ip = []
    dico_subdomain_per_ip = {}
    dico_ip_per_subdomain = {}
    for file in liste_file_to_merge:
        file_path = f"{dir_path}{file}"
        print(file_path)
        with open(file_path) as file:
            data_file = file.read()
            if data_file:
                object_data = '{"data":'+ str(data_file)+'}'
                data = json.loads(object_data).get('data')
        if data_file:
            for elem in data:
                print(type(elem))
                if elem['type'] == "A":
                    ip = elem['address']

                    liste_ip.append(ip)
                    if ip not in dico_subdomain_per_ip.keys():
                        dico_subdomain_per_ip[ip] = []
                    sub_domain = elem['domain']
                    dico_subdomain_per_ip[ip].append(sub_domain)
                
    liste_ip = list(set(liste_ip))
    return dico_subdomain_per_ip

def get_ip_from_sub_domains(domain_name,sub_domain_list,repertory_path):
    GREEN = '\033[0;32m'
    BLUE = "\033[0;34m"
    COLOR_OFF = "\033[0m"

    print(f"{BLUE}Execution DNS Recon{COLOR_OFF}")
    dir_path = f"{repertory_path}/{domain_name}/dns-recon/"
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    for sub_domain in sub_domain_list:
        sub_domain = sub_domain.rstrip()
        output_path = f"{dir_path}/{sub_domain}-dns_recon.json"
        command = f'nohup dnsrecon -d {sub_domain} -t std -j {output_path}'
        result = subprocess.run(command,stderr=subprocess.PIPE, shell=True, executable="/bin/bash")
        print(f"[ {GREEN}+{COLOR_OFF} ] {sub_domain}")
    return merge_ip_into_single_file(dir_path)