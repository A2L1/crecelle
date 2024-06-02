from utils import (get_ip_from_sub_domains,lauch_subfinder)
import os
import json

class Project:
    
    
    def __init__(self,name_project):
        self.name = name_project
        self.loaded_subdomain = []
        self.loaded_subdomain_per_ip = {}
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