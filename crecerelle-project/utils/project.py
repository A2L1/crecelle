from utils import (get_ip_from_sub_domains,lauch_subfinder,launch_nmap_scan_list,launch_nmap_scan_input,format_data,launch_searchploit)
import os
import json

class Project:
    

    def __init__(self,name_project):
        self.name = name_project
        self.loaded_subdomain = []
        self.loaded_subdomain_per_ip = {}
        self.loaded_scan_name_from_subdomain_scan = ""
        self.loaded_scan_nmap = {}
        self.loaded_scan_name_from_nmap_scan = ""
        self.loaded_scan_path_from_nmap_scan = ""
        self.repertory_content = []
        self.repertory_path = self.check_existence_of_folder_project()

    def check_existence_of_folder_project(self):
        
        tried_path = f'/crecerelle-project/utils/load/{self.name}'
        if not os.path.isdir(tried_path):
            print(f"Création du dossier de sauvegarde du projet {self.name}")
            os.makedirs(tried_path)
        else:
            print(f"Le projet {self.name} à bien été cherché depuis le chemin : {tried_path}")
        project_dir = os.listdir(tried_path)
        self.repertory_content = project_dir
        return tried_path

    def load_dns_backup(self,path): 
        
        subdomain_list =[]
        try :
            with open(path,"r") as f:
                data = f.readlines()
                f.close()
        except FileNotFoundError as e:
            print(f"Aucun fichier n'existe {path}")
            return 0
        for line in data:
            subdomain_list.append(line.rstrip())

        self.loaded_subdomain = subdomain_list

    def load_ip_sublist_backup(self,domain_name):
        BLUE = "\033[0;34m"
        COLOR_OFF = "\033[0m"

        file_path = f"{self.repertory_path}/{domain_name}/dns-recon/{domain_name}_dns_recon_backup.json"
        
        with open(file_path,'r') as file:
            ip_subdomain_obj = json.load(file)

        self.loaded_subdomain_per_ip = ip_subdomain_obj
        self.loaded_scan_name_from_subdomain_scan = domain_name

        print(f"{BLUE}Le fichier concernant le scan '{domain_name}' est chargé.{COLOR_OFF}")

    def new_subfinder_search(self,domain):
        file_path = lauch_subfinder(domain,self.name,self.repertory_path)
        self.load_dns_backup(file_path)

    def get_list_ip_from_subdomain(self,domain_name):
        BLUE = "\033[0;34m"
        COLOR_OFF = "\033[0m"

        json_subdomain_per_ip = get_ip_from_sub_domains(domain_name,sub_domain_list=self.loaded_subdomain,repertory_path=self.repertory_path)
        print(json_subdomain_per_ip)
        self.loaded_subdomain_per_ip = json_subdomain_per_ip
        backup_file = f"{self.repertory_path}/{domain_name}/dns-recon/{domain_name}_dns_recon_backup.json"
        print(f"{BLUE}Le fichier de backup est disponible à ce chemin : {backup_file}{COLOR_OFF}")
        with open(backup_file, 'w', encoding='utf-8') as fichier:
            json.dump(json_subdomain_per_ip, fichier, ensure_ascii=False, indent=4)

    def launch_nmap_scan(self,list_ip_subdomain={},target_ip="",answer_load_or_input={}):

        match answer_load_or_input:
            case "1":
                check_scan = self.loaded_scan_name_from_subdomain_scan
            case "2":
                check_scan = target_ip.replace("/","-")

        if not os.path.isdir(f'{self.repertory_path}/{check_scan}/nmap'):
            os.makedirs(f'{self.repertory_path}/{check_scan}/nmap')

        
        match answer_load_or_input:
            case "1":
                launch_nmap_scan_list(list_ip_subdomain,scan_name=check_scan,directory_save_path=self.repertory_path)
            case "2":
                launch_nmap_scan_input(target_ip,scan_name=check_scan,directory_save_path=self.repertory_path)

    def load_base_searchsploit_data(self,scan):
        BLUE = "\033[0;34m"
        COLOR_OFF = "\033[0m"

        file_path = f"{self.repertory_path}/{scan}/nmap/{scan}-nmap.json"
        

        with open(file_path,'r') as file:
            port_with_version_per_ip = json.load(file)

        self.loaded_subdomain_per_ip = port_with_version_per_ip
        self.loaded_scan_name_from_nmap_scan = scan
        self.loaded_scan_path_from_nmap_scan = file_path

        print(f"{BLUE}Le fichier concernant le scan '{scan}' est chargé.{COLOR_OFF}")

    def launch_searchsploit_scan(self,scan_name):
        
        self.load_base_searchsploit_data(scan_name)
        
        formated_data = format_data(self.loaded_scan_path_from_nmap_scan)

        launch_searchploit(data=formated_data,repertory_path=self.repertory_path,scan_name=self.loaded_scan_name_from_nmap_scan)
