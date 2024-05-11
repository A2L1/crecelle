from utils import (get_ip_from_sub_domains,lauch_subfinder)
import os

class Project:
    
    
    def __init__(self,name_project):
        self.name = name_project
        self.loaded_dns = []
        self.repertory_content = []
        self.repertory_path = self.check_existence_of_folder_project()

    def check_existence_of_folder_project(self):
        
        tried_path = f'/crecelle-project/utils/load/{self.name}'
        if not os.path.isdir(tried_path):
            print(f"Création du dossier de sauvegarde du projet {self.name}")
            os.makedirs(tried_path)
        else:
            print(f"Le projet {self.name} à bien été cherché depuis le chemin : {tried_path}")
        project_dir = os.listdir(tried_path)
        self.repertory_content = project_dir
        return tried_path

    def load_dns_backup(self):
        print('')
        # try :
            # file_path = f'load/{self.name}/{self.name}'
            # open()
        # slef.loade_dns == content(file)
        # Else       
        
        return [self.name]

    def new_subfinder_search(self,domain):
        subdomain_list = lauch_subfinder(domain,self.name)
        print(subdomain_list)
        return subdomain_list

    