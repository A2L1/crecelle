from utils.project import Project
from utils import create_or_load_project,kill_chain_step_choice,recon_on_ip_domain,banner,choice_load_or_input_ip

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

            match answer_domain_ip:
                case "1":
                    print("choix 1")

            print("nmap")
        case "@":
            exit = 1

print("Sortie du programme")