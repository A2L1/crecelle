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
        f = open(file_path)
        text = f.read()
        data = json.loads(text)
        print(data)
        f.close()
        for elem in data:
            if elem['type'] == "A":
                ip = elem['address']

                liste_ip.append(ip)
                if ip not in dico_subdomain_per_ip.keys():
                    dico_subdomain_per_ip[ip] = []
                sub_domain = elem['domain']
                dico_subdomain_per_ip[ip].append(sub_domain)
                
    liste_ip = list(set(liste_ip))
    print(liste_ip)
    print(dico_subdomain_per_ip)

def get_ip_from_sub_domains(file,name):
    print("Execution DNS Recon")

    with open(file,'r') as f:
        data=f.readlines()
        # print(data)
        f.close() 
        
    for sub_domain in data:
        index_of_sub = data.index(sub_domain)
        sub_domain = sub_domain.rstrip()
        dir_path = "out/dns_recon/"
        output_path = f"{dir_path}{name}{index_of_sub}-dns_recon.json"
        command = f'dnsrecon -d {sub_domain} -t std -j {output_path}'
        # print(command)
        result = subprocess.run(command,stderr=subprocess.PIPE, shell=True, executable="/bin/bash")
    merge_ip_into_single_file(dir_path)