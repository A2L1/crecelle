#!/bin/python3

from utils.project import Project
from utils import wipe_text,create_or_load_project,kill_chain_step_choice,recon_on_ip_domain,banner,choice_load_or_input_ip,choice_file_to_load,choice_nmap_to_load

print("\033c")

banner()

project_name = create_or_load_project()

project = Project(project_name)


exit = 0

while not exit:
    answer = kill_chain_step_choice()
    match answer:
        case "1":
            answer_domain_ip = recon_on_ip_domain()
            match answer_domain_ip:
                case "1":
                    domain_name = input("Sélectionnez un nom de domaine: \n")
                    project.new_subfinder_search(domain_name)
                    project.get_list_ip_from_subdomain(domain_name)
        case "2":
            answer_load_or_input = choice_load_or_input_ip()
            match answer_load_or_input:
                case "1":
                    file_name = choice_file_to_load(project_name=project.name)

                    if not file_name:
                        print("Pas de scan de domaine disponible")
                        print("Effectuez une partie reconnaissance")
                        wipe_text(sleep=3)
                    else:
                        project.load_ip_sublist_backup(file_name)
                        project.launch_nmap_scan(list_ip_subdomain=project.loaded_subdomain_per_ip,answer_load_or_input=answer_load_or_input)
                case "2":
                    ip = input("Saisissez une IP: \n") # à factoriser et vérifier regex d'une ip
                    project.launch_nmap_scan(target_ip=ip,answer_load_or_input=answer_load_or_input)
        case "3":
            answer_nmap_to_load = choice_nmap_to_load(project_name=project.name)
            if not answer_nmap_to_load:
                print("Pas de scan Nmap disponible")
                print("Effectuez une partie Enumeration")
                wipe_text(sleep=2)
            else:
                project.launch_searchsploit_scan(answer_nmap_to_load)
                wipe_text(3)
        case "@":
            exit = 1

print("Sortie du programme")